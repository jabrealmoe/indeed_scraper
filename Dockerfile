# Dockerfile for Indeed Scraper with PostgreSQL
FROM python:3.12-slim

# Install system dependencies (psycopg2 needs gcc, libpq-dev)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose a default command (can be overridden)
ENTRYPOINT ["python", "cli.py"]
