"""Image generation client — wraps FAL.ai / OpenAI image API for LINE replies."""

from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass
from pathlib import Path

import httpx

logger = logging.getLogger("image_client")

# FAL.ai API (default)
FAL_BASE_URL = "https://api.fal.ai"
FAL_MODEL = "black-forest-labs/flux-1-dev"

# LINE image constraints
LINE_IMAGE_MAX_SIZE_BYTES = 30 * 1024 * 1024  # 30MB
LINE_IMAGE_MAX_WIDTH = 1024
LINE_IMAGE_MAX_HEIGHT = 1024


@dataclass
class ImageResult:
    path: Path
    mime: str = "image/jpeg"
    width: int = 1024
    height: int = 1024


def generate_image(
    prompt: str,
    *,
    aspect_ratio: str = "landscape",
    output_dir: Path | None = None,
) -> ImageResult | None:
    """Generate an image from a text prompt via FAL.ai API."""
    if output_dir is None:
        output_dir = Path("/tmp/images")
    output_dir.mkdir(parents=True, exist_ok=True)

    token = uuid.uuid4().hex[:16]
    dest = output_dir / f"{token}.jpg"

    # Map aspect ratio to dimensions
    size_map = {
        "landscape": (1024, 768),
        "square": (1024, 1024),
        "portrait": (768, 1024),
    }
    width, height = size_map.get(aspect_ratio, (1024, 768))

    try:
        with httpx.Client(timeout=120.0) as client:
            resp = client.post(
                f"{FAL_BASE_URL}/v1/images/generations",
                json={
                    "model": FAL_MODEL,
                    "prompt": prompt,
                    "width": width,
                    "height": height,
                    "size": "1024x768",
                },
                headers={
                    "Authorization": f"Bearer {get_fal_api_key()}",
                    "Content-Type": "application/json",
                },
            )
            resp.raise_for_status()
            payload = resp.json()

        # Extract image URL from response
        images = payload.get("data", [])
        if images:
            image_url = images[0].get("url")
            if image_url:
                # Download the image
                with httpx.Client(timeout=30.0) as client:
                    img_resp = client.get(image_url)
                    img_resp.raise_for_status()
                    dest.write_bytes(img_resp.content)

                logger.info(
                    "Image generated: %s (%d bytes, %dx%d)",
                    dest.name, dest.stat().st_size, width, height,
                )
                return ImageResult(path=dest, width=width, height=height)

    except Exception as exc:
        logger.error("Image generation failed for '%s': %s", prompt[:50], exc)

    return None


def get_fal_api_key() -> str:
    """Get FAL.ai API key from environment."""
    import os
    return os.environ.get("FAL_KEY", "")


def should_generate_image(
    text_prompt: str,
    *,
    min_words: int = 5,
) -> bool:
    """Heuristic: generate image if the prompt suggests visual content."""
    image_keywords = [
        "show", "draw", "picture", "image", "photo", "diagram",
        "illustrate", "visualize", "sketch", "painting", "icon",
        "logo", "banner", "thumbnail", "screenshot", "chart",
        "graph", "map", "poster", "cover", "avatar",
    ]
    lower = text_prompt.lower()
    return any(kw in lower for kw in image_keywords) and len(text_prompt.split()) >= min_words


def build_line_image_message(
    image_result: ImageResult,
    public_url: str,
) -> dict:
    """Build LINE image message object."""
    return {
        "type": "image",
        "originalContentUrl": f"{public_url}/images/{image_result.path.name}",
        "previewImageUrl": f"{public_url}/images/{image_result.path.name}",
    }