# Indeed Job Scraper

A production-quality, reusable Python CLI application that scrapes job listings from Indeed.

## Features

- **CLI Interface**: Parameterized execution using `click`.
- **Robust Scraping**: Handles pagination, retries with exponential backoff (`tenacity`), and randomizes User-Agent (`fake-useragent`).
- **Data Parsing**: Extracts title, company, location, date, summary, and link using `BeautifulSoup`.
- **Output Formats**: Exports to CSV or JSON.
- **Logging**: Structured logging for debugging and monitoring.

## Installation

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scraper using the module syntax:

```bash
python indeed_scraper.py --query "python developer" --city "New York, NY" --days 3 --pages 2 --output jobs.csv
```

### Parameters

| Parameter  | Description                      | Default    | Example               |
| ---------- | -------------------------------- | ---------- | --------------------- |
| `--query`  | Job search keywords              | Required   | `"data scientist"`    |
| `--city`   | City/Location                    | Required   | `"San Francisco, CA"` |
| `--days`   | Jobs posted within last N days   | `7`        | `3`                   |
| `--pages`  | Number of result pages to scrape | `5`        | `10`                  |
| `--output` | Output filename                  | `jobs.csv` | `results.json`        |
| `--format` | Output format (`csv` or `json`)  | `csv`      | `json`                |

## Project Structure

```
indeed_scraper/
├── __init__.py
├── cli.py        # Entry point for the CLI
├── scraper.py    # Scraping orchestration and requests
├── parser.py     # HTML parsing logic
├── models.py     # Data structures
└── utils.py      # Helpers (retries, headers, logging)
```

## Note on Scraping Indeed

Indeed employs strict anti-bot measures. This scraper uses:

- Randomized User-Agents
- Random delays between requests
- Retry logic

However, if you scrape too aggressively, you may interpret CAPTCHAs or be blocked. Increase delays or use a proxy service (not included) for heavy usage.
