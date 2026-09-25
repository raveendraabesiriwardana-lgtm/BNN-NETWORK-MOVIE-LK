import requests
from bs4 import BeautifulSoup
import json
import os

movies_data = []

# Header to avoid bot blocking
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def scrape_sinhalasub():
    try:
        url = "https://sinhalasub.lk/"
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Select movie blocks
        items = soup.find_all('article', class_='item', limit=12)
        for item in items:
            title = item.find('h3').text.strip() if item.find('h3') else "Movie"
            poster = item.find('img')['src'] if item.find('img') else ""
            link = item.find('a')['href'] if item.find('a') else "#"
            
            movies_data.append({
                "title": title,
                "poster": poster,
                "download_link": link,
                "source": "SinhalaSub.LK",
                "source_code": "sinhalasub"
            })
    except Exception as e:
        print(f"Error scraping SinhalaSub: {e}")

def scrape_baiscope():
    try:
        url = "https://www.baiscopelk.com/"
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        posts = soup.find_all('article', limit=12)
        for post in posts:
            title_elem = post.find('h2', class_='entry-title')
            if title_elem and title_elem.find('a'):
                title = title_elem.find('a').text.strip()
                link = title_elem.find('a')['href']
                img = post.find('img')
                poster = img['src'] if img else "https://via.placeholder.com/200x280"
                
                movies_data.append({
                    "title": title,
                    "poster": poster,
                    "download_link": link,
                    "source": "Baiscope",
                    "source_code": "baiscope"
                })
    except Exception as e:
        print(f"Error scraping Baiscope: {e}")

# Execute Scraping
print("Scraping Movies...")
scrape_sinhalasub()
scrape_baiscope()

# Save to movies.json
with open('movies.json', 'w', encoding='utf-8') as f:
    json.dump(movies_data, f, ensure_ascii=False, indent=4)

print("Saved movies to movies.json successfully!")
