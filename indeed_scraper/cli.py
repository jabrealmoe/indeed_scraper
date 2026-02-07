import click
import pandas as pd
import json
import os
from .scraper import IndeedScraper
from .utils import setup_logger
from .models import Job

logger = setup_logger("cli")

@click.command()
@click.option('--query', required=True, help='Job search keywords (e.g., "python developer")')
@click.option('--city', required=True, help='City name (e.g., "Atlanta, GA")')
@click.option('--days', default=7, help='Jobs posted within last N days')
@click.option('--pages', default=5, help='Number of result pages to scrape')
@click.option('--output', default='jobs.csv', help='Output file name')
@click.option('--format', type=click.Choice(['csv', 'json'], case_sensitive=False), default='csv', help='Output format')
def main(query, city, days, pages, output, format):
    """
    Indeed Job Scraper CLI.
    
    Scrapes job listings from Indeed based on search criteria.
    """
    logger.info(f"Starting scrape: query='{query}', city='{city}', days={days}, pages={pages}")
    
    scraper = IndeedScraper()
    jobs = scraper.scrape(query=query, city=city, days=days, pages=pages)
    
    if not jobs:
        logger.warning("No jobs found. Exiting.")
        return

    # Convert to DataFrame
    job_dicts = [job.to_dict() for job in jobs]
    df = pd.DataFrame(job_dicts)
    
    # Export
    output = validate_extension(output, format)
    if format == 'csv':
        df.to_csv(output, index=False)
        logger.info(f"Saved {len(jobs)} jobs to {output}")
    elif format == 'json':
        df.to_json(output, orient='records', indent=2)
        logger.info(f"Saved {len(jobs)} jobs to {output}")

def validate_extension(filename, format):
    """Ensures filename has the correct extension."""
    base, ext = os.path.splitext(filename)
    expected_ext = f".{format}"
    if ext.lower() != expected_ext:
        return f"{base}{expected_ext}"
    return filename

if __name__ == '__main__':
    main()
