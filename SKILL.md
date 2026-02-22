name: indeed_scraper
description: Automated job searching on Indeed and AI-driven resume customization.
icon: icon.png
---

# Indeed Scraper Skill

This skill allows you to search for jobs on Indeed and generate tailored resumes using AI.

## Tools

### scrape
Search for job listings on Indeed.

**Parameters:**
- `query` (required): Job titles or keywords.
- `city` (required): Location (e.g., "Austin, TX", "Remote").
- `days` (optional): Number of days back to search (default: 7).
- `pages` (optional): Number of pages to scrape (default: 5).

**Implementation:**
```bash
./scripts/scrape.sh "$query" "$city" "$days" "$pages"
```

### generate
Generate a customized resume for a job listing.

**Parameters:**
- `input` (required): Path to the scraped jobs file (e.g., "output/jobs.csv").
- `resume` (required): Path to your base resume file (e.g., "my_resume.txt").
- `model` (optional): Ollama model name (default: "llama3.2").

**Implementation:**
```bash
./scripts/generate.sh "$input" "$resume" "$model"
```
