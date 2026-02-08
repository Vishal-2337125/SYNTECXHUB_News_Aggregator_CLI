import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class HeadlineFetcher:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def get_headlines(self, url):
        """Extracts text and URLs from news elements."""
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []

            # Targeting elements commonly used for headlines
            for item in soup.find_all(['h1', 'h2', 'h3', 'a']):
                title_text = item.get_text(strip=True)
                link = item if item.name == 'a' else item.find('a')
                
                if link and link.has_attr('href') and len(title_text) > 20:
                    results.append({
                        'headline': title_text,
                        'url': urljoin(url, link['href'])
                    })
            
            # Remove duplicates within the current scrape
            return list({each['url']: each for each in results}.values())
        except Exception as e:
            print(f"Scraping Error: {e}")
            return []