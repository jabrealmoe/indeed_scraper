---
name: Cost Priority and Local LLMs Rules
description: Enforce usage of Ollama & free models.
---

# Agent Instructions for `indeed_scraper` (OpenClaw / Any Other AI Agent)

1. **COST IS THE ABSOLUTE FIRST PRIORITY.** Do not spend API credits for generation or semantic embeddings.
2. Ensure you *only* propose **Ollama local models** (reachable on `http://localhost:11434` or as part of the `docker-compose` stack).
3. We are building a sophisticated but *totally free* pipeline by storing high-dimensional vectors (from job descriptions mapping back to our candidate profile) into `pgvector` inside PostgreSQL.
4. **Never rely on the OpenAI pip package** or Anthropic endpoints unless the user forces you to bypass this rule because they are specifically setting an `OPENAI_API_KEY` for a one-off reason.
5. Emphasize self-sufficient architectures: PostgreSQL for relations & similarity search. Scrape locally, Embed locally (e.g. `nomic-embed-text`), Generate locally (e.g. `llama3.2`).
