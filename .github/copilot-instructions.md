# GitHub Copilot Instructions

**CRITICAL PRIORITY: Zero Cost / Open Source Models FIRST.**

1. **Local over Cloud**: Whenever generating code that interacts with intelligence, embeddings, or language, default immediately to `ollama` endpoints (e.g. `http://localhost:11434/api/generate` or `/api/embed`).
2. **Never Propose Paid APIs Setup Unless Explicitly Asked**: Do not prompt to use `openai.Embedding.create()` or `anthropic.Anthropic()`.
3. **Use Local Libraries HuggingFace / Transformers**: If offline LLM via Ollama is unavailable, guide the user to `sentence-transformers` or other completely offline, free, open-source models with permissive licenses.
4. **Assume Postgres for Vector Storage**: Always lean on `pgvector` inside a Docker container (as seen in `docker-compose.yml`) rather than Pinecone, Weaviate Cloud, or other paid/SaaS vector stores.
