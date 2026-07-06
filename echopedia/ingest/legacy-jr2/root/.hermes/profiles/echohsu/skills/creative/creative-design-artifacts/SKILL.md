---
name: creative-design-artifacts
description: "Umbrella for visual/design artifacts: HTML mockups, design systems, diagrams, Excalidraw, p5.js, Manim, and creative coding."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [design, html, diagrams, creative-coding, visualization, p5js, manim, excalidraw, ui]
---

# Creative Design Artifacts

Use this umbrella for user-visible visual artifacts: UI mockups, landing pages, design systems, diagrams, infographics, Excalidraw boards, p5.js sketches, Manim videos, creative browser demos, and text/ASCII art.

## Route by artifact type

- **HTML/UI artifact**: produce a standalone HTML/CSS/JS file; use known design-system references when the user names a brand style.
- **Disposable sketch**: create 2–3 variants quickly so the user can compare directions; avoid over-engineering.
- **Architecture/flow diagram**: choose SVG/HTML for polished dark technical diagrams or Excalidraw JSON for hand-drawn editable diagrams.
- **Infographic/comic/educational visual**: identify the information structure first, then choose layout and style.
- **Creative coding**: use p5.js/Pretext/TouchDesigner when interactivity, generative motion, typography, particles, GLSL, or live visuals matter.
- **Educational animation**: use Manim when the core value is mathematical/geometric explanation over static design.
- **ASCII/text art**: use local text-art tools for terminal-native output or lightweight visual jokes.

## Quality bar

1. Clarify the intended medium, audience, aspect ratio, and editability only if not obvious.
2. Produce an actual artifact file or generated media, not a description.
3. Use semantic structure, consistent spacing, accessible contrast, and deliberate visual hierarchy.
4. Verify the artifact can be opened/rendered or that generated media exists.
5. When support files or templates are needed, keep them inside the active skill package and reference paths explicitly.

## Absorbed domain notes

- **Claude-style design**: preserve taste and interaction polish without assuming a hosted Claude Design environment.
- **Popular web designs / DESIGN.md**: useful when the user wants a recognizable brand-like system or token spec.
- **Architecture diagrams / Excalidraw**: both are diagramming workflows; choose polished SVG/HTML vs editable hand-drawn JSON.
- **p5.js / Pretext / TouchDesigner**: creative coding families; start from a minimal working sketch and iterate with visual verification.
- **Manim**: storyboard the conceptual reveal before writing code.
- **Humanizer**: for prose artifacts, remove AI-ish patterns and preserve the author's voice.

## Consolidated subworkflows

Use these labeled subsections instead of loading one narrow skill per artifact family:

### Polished technical diagrams
- For architecture/cloud/infra diagrams, create a standalone dark-themed HTML/SVG artifact with explicit labels, layout groups, arrows, and legend.
- For hand-drawn editable boards, emit valid Excalidraw JSON and verify it imports; use a rougher visual language for brainstorming and sequence/flow diagrams.

### HTML mockups and design systems
- For quick comparison work, build 2–3 throwaway HTML variants with different layout/tone choices and make the trade-offs visible.
- For production-style one-offs, use polished single-file HTML/CSS/JS with responsive spacing, typography, and accessibility checks.
- When the user names a brand or product style, borrow design-system principles and tokens rather than copying proprietary assets.
- For DESIGN.md requests, author token/spec content as a design-system artifact and validate the file shape before reporting completion.

### Infographics and knowledge visuals
- Before drawing, classify the content structure: timeline, comparison matrix, funnel, iceberg, map, process, hierarchy, causal loop, or dashboard.
- Pair layout with a coherent palette and visual metaphor; avoid cramming prose into the image.
- For Chinese/knowledge-comic style artifacts, preserve original terminology and plan panel-by-panel explanation before generating visuals.

### Creative coding and live visuals
- For p5.js, Pretext, and TouchDesigner-style work, start with a minimal running sketch, then iterate with visual verification.
- Use p5.js for generative art, animation, shaders, exports, and browser interactivity.
- Use Pretext for DOM-free text layout, kinetic typography, text-as-geometry, and flow-around-obstacles demos.
- Use TouchDesigner/MCP only when a live TouchDesigner instance is available; otherwise provide a reproducible node/network plan or fallback HTML sketch.

### Educational animation and text art
- Use Manim when the learning value comes from staged mathematical/geometric reveals; storyboard first, then render a small scene to verify.
- Use ASCII/text-art tools for terminal-native banners, diagrams, jokes, or image-to-ASCII conversions.

### Prose humanization
- Preserve factual meaning and the user’s voice; remove AI-ish throat-clearing, symmetry, filler transitions, and generic conclusions.
- Do not “humanize” by adding unsupported anecdotes or weakening technical precision.