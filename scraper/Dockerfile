# Use an appropriate base image with Python and scrapy installed
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /scraper

# Copy the scraper code into the container
COPY . /scraper

# Install any dependencies required for the scraper
RUN pip install -r requirements.txt

# Command to run the scraper
CMD ["scrapy", "crawl", "sreality", "-O", "/data/results.json"]

