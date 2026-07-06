# Portrait Image-to-Video Reference Workflow

Use this when the user wants a short video generated from a real person's approved/reference photo, especially documentary or commemorative portrait clips.

## Goal

Preserve identity and dignity while adding subtle cinematic motion. For specific real people, prefer image-to-video over pure text-to-video.

## Recommended sequence

1. Confirm or infer the uploaded image is the intended reference when the user explicitly says to use it.
2. Treat the source photo as the identity/start-frame reference.
3. Generate or refine a still keyframe first when the target background/style differs significantly from the source photo.
4. Run an image-to-video workflow/model with low-to-medium motion.
5. Add readable text overlays in post-production rather than relying on the video model to render text.
6. Review outputs for face consistency, glasses/eyes stability, natural blinking, and respectful tone.

## Prompt pattern

Positive prompt:

> Use the provided reference photo of [person]. Preserve facial identity, glasses, natural expression, and dignified appearance. Create a realistic [duration]-second cinematic documentary-style video. [Describe setting/background]. Soft warm light, shallow depth of field, subtle dust particles. Camera slowly pushes in. The subject gently turns toward the lens and gives a calm, knowing smile. Natural blinking, minimal motion, respectful tone.

Negative prompt:

> distorted face, changed identity, warped glasses, melting face, uneven eyes, exaggerated smile, fake teeth, extra limbs, cartoon style, anime, glitch artifacts, unreadable text, overdramatic motion, low quality, blurry face

## Settings guidance

- Duration: 5–6 seconds for portrait clips.
- Motion strength: low to medium.
- Camera: slow push-in or very subtle parallax.
- Identity/face preservation: high.
- Avoid mouth movement unless lip-sync is explicitly requested.
- Add final captions separately with an editor or ffmpeg.

## Verification checklist

- Face identity remains stable across the clip.
- Glasses, eyes, and smile do not warp.
- No extra limbs or background artifacts distract from the subject.
- Any text overlay is added in post and is legible.
- The clip’s tone is respectful and culturally appropriate for commemorative/historical content.
