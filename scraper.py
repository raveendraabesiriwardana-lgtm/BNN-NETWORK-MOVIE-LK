import requests
from bs4 import BeautifulSoup
import json

movies_data = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 1. SinhalaSub.LK
def scrape_sinhalasub():
    try:
        url = "https://sinhalasub.lk/"
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        items = soup.select('article.item, div.result-item, .post')
        for item in items[:15]:
            title_elem = item.find('h3') or item.find('h2') or item.find('a')
            img_elem = item.find('img')
            link_elem = item.find('a')
            
            if title_elem and link_elem:
                title = title_elem.text.strip()
                link = link_elem.get('href', '#')
                poster = img_elem.get('src', '') if img_elem else 'https://via.placeholder.com/200x280'
                
                movies_data.append({
                    "title": title,
                    "poster": poster,
                    "download_link": link,
                    "source": "SinhalaSub.LK",
                    "source_code": "sinhalasub"
                })
    except Exception as e:
        print(f"Error scraping SinhalaSub: {e}")

# 2. Baiscope Sinhala
def scrape_baiscope():
    try:
        url = "https://www.baiscopelk.com/"
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        posts = soup.select('article, .post')
        for post in posts[:15]:
            title_elem = post.select_one('.entry-title a, h2 a')
            img_elem = post.find('img')
            
            if title_elem:
                title = title_elem.text.strip()
                link = title_elem.get('href', '#')
                poster = img_elem.get('src', '') if img_elem else 'https://via.placeholder.com/200x280'
                
                movies_data.append({
                    "title": title,
                    "poster": poster,
                    "download_link": link,
                    "source": "Baiscope Sinhala",
                    "source_code": "baiscope"
                })
    except Exception as e:
        print(f"Error scraping Baiscope: {e}")

# 3. Subz LK
def scrape_subz():
    try:
        url = "https://subz.lk/"
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        posts = soup.select('article, .post')
        for post in posts[:15]:
            title_elem = post.select_one('.entry-title a, h2 a, h3 a')
            img_elem = post.find('img')
            
            if title_elem:
                title = title_elem.text.strip()
                link = title_elem.get('href', '#')
                poster = img_elem.get('src', '') if img_elem else 'https://via.placeholder.com/200x280'
                
                movies_data.append({
                    "title": title,
                    "poster": poster,
                    "download_link": link,
                    "source": "Subz LK",
                    "source_code": "subz"
                })
    except Exception as e:
        print(f"Error scraping Subz: {e}")

print("Scraping started...")
scrape_sinhalasub()
scrape_baiscope()
scrape_subz()

# Save output
with open('movies.json', 'w', encoding='utf-8') as f:
    json.dump(movies_data, f, ensure_ascii=False, indent=4)

print(f"Successfully scraped {len(movies_data)} movies and saved to movies.json!")
