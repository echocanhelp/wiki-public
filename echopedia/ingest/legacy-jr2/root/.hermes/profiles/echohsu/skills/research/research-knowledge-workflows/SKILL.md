---
name: research-knowledge-workflows
description: "Umbrella for research discovery, paper workflows, feeds, prediction markets, and durable knowledge bases."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, arxiv, papers, feeds, llm-wiki, prediction-markets, knowledge-base]
---

# Research & Knowledge Workflows

Use this class-level skill for research tasks: finding papers, writing/reviewing papers, monitoring feeds, querying prediction markets, and building persistent markdown knowledge bases.

## Route by task

- **Paper discovery**: use arXiv and web/scholarly sources; collect title/authors/date/URL/abstract and note limitations.
- **Research paper writing**: structure claims, experiments, citations, related work, ablations, and venue-specific checklists.
- **Feed monitoring**: use RSS/blog tooling for recurring source tracking and read/unread state.
- **Knowledge base building**: create interlinked markdown notes that compound over time; prefer stable concepts and citations over one-off dumps.
- **Prediction markets**: query market metadata, prices, order books, and history; report as market-implied probabilities, not truth.

## Procedure

1. Define the research question and output format.
2. Gather sources with provenance and timestamps.
3. Synthesize: separate evidence, interpretation, and uncertainty.
4. Save or return a structured artifact when requested: bibliography, markdown wiki page, literature matrix, market table, or draft section.
5. Verify links/identifiers and avoid unsupported claims.

## Pitfalls

- Search APIs have coverage gaps; absence from one source is not absence overall.
- Prediction market liquidity and wording matter; read the exact market resolution criteria.
- Knowledge bases should be curated and linked, not raw transcript dumps.

## Consolidated research/tool subworkflows

### arXiv and paper discovery
- Use arXiv for fast paper lookup by keyword, author, category, or ID; record title, authors, date, abstract, primary category, and canonical URL.
- For literature review, combine arXiv with web/scholar/source checks and separate discovery metadata from synthesis.

### Research paper writing
- Treat venue templates/checklists as support material under the paper-writing workflow, not separate task classes.
- Maintain the chain from claim → evidence → experiment/ablation → citation. Use venue-specific templates only after the argument and contribution are clear.

### Prediction markets
- Polymarket queries are research evidence about market-implied beliefs. Read resolution criteria, liquidity, order books/history, and timestamp; do not present prices as facts about the world.