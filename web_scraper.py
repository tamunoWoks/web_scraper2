"""
A basic Python script that scrapes data from a website.

PIP INSTALLATIONS:
pip install requests
pip install beautifulsoup4
pip install validators

"""

# Import necessary modules
import requests
from bs4 import BeautifulSoup
import validators

def scrape_website(url):
    """
    Scrapes basic content (headings, paragraphs, images, links) from a given URL.
    """
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")
