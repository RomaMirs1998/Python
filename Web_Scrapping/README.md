# Hacker News Scraper

A Python-based web scraper that fetches top stories from [Hacker News](https://news.ycombinator.com/news) based on their vote count.

## Features:
    1. Grabs articles from the first two pages of Hacker News.
    2. Filters out articles with less than 100 votes.
    3. Sorts articles by votes in descending order.
    4. Displays the title, link, and vote count of the top articles.

## Requirements:
- Python 3.x
- `requests` module (install via pip: `pip install requests`)
- `BeautifulSoup4` module (install via pip: `pip install beautifulsoup4`)

## Usage:

To run the script and fetch top stories:

python scrape.py

Once executed, the script will display the top stories from Hacker News that have more than 100 votes, sorted by vote count in descending order.

## How it works:

    1. The script sends a request to fetch the HTML content of the first two pages of Hacker News.
    2. Using BeautifulSoup, it parses the HTML and extracts the relevant data (links, titles, and vote count).
    3. It then filters out stories with less than 100 votes and sorts the remaining stories based on vote count.
    4. Finally, it displays the sorted list of top stories.

## Notes:
- Web scraping can be subject to terms of service of the website. Always ensure you have the right to scrape a website and be respectful by not sending too many requests in a short time.
- The structure of websites can change over time. If the script stops working, the HTML structure of Hacker News might have changed, and the script might need updating.
