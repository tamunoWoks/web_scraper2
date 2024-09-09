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

        # Scrape headings (h1, h2, h3, etc.)
        for heading_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = soup.find_all(heading_tag)
            if headings:
                print(f"\n{heading_tag.upper()} Tags:")
                for heading in headings:
                    print(heading.get_text().strip())

        # Scrape all paragraphs
        paragraphs = soup.find_all('p')
        if paragraphs:
            print("\nParagraphs:")
            for para in paragraphs:
                print(para.get_text().strip())

        # Scrape all images
        images = soup.find_all('img')
        if images:
            print("\nImages:")
            for img in images:
                img_src = img.get('src')
                alt_text = img.get('alt', 'No alt text')
                print(f"Image Source: {img_src}, Alt Text: {alt_text}")

        # Scrape all links
        links = soup.find_all('a')
        if links:
            print("\nLinks:")
            for link in links:
                href = link.get('href')
                link_text = link.get_text().strip()
                print(f"Link Text: {link_text}, URL: {href}")
