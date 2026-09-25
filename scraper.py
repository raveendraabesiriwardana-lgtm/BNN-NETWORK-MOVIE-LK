import requests
from bs4 import BeautifulSoup
import json

movies_data = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_cinesubz():
    try:
        url = "https://cinesubz.co/"
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Select items from main page
        articles = soup.select('article')
        
        for article in articles[:15]:  # Latest 15 movies
            title_elem = article.select_one('.entry-title a, h2 a, h3 a')
            img_elem = article.find('img')
            
            if title_elem:
                title = title_elem.text.strip()
                page_url = title_elem.get('href', '#')
                poster = img_elem.get('src', '') if img_elem else ''
                
                # Scraping Direct Download Links from Movie Detail Page
                download_links = []
                try:
                    movie_resp = requests.get(page_url, headers=headers, timeout=10)
                    movie_soup = BeautifulSoup(movie_resp.text, 'html.parser')
                    
                    # Find download buttons
                    dl_blocks = movie_soup.select('a.maxbutton, a[href*="direct"], a.btn, div.download-link a')
                    for btn in dl_blocks:
                        link_url = btn.get('href', '')
                        btn_text = btn.text.strip()
                        if link_url and ('http' in link_url):
                            download_links.append({
                                "quality": btn_text if btn_text else "Direct Download",
                                "size": "Direct Link",
                                "url": link_url
                            })
                except Exception as inner_e:
                    print(f"Error fetching detail page for {title}: {inner_e}")

                movies_data.append({
                    "title": title,
                    "poster": poster,
                    "page_url": page_url,
                    "download_links": download_links
                })

    except Exception as e:
        print(f"Error scraping CineSubz: {e}")

print("Scraping CineSubz...")
scrape_cinesubz()

# Save output to movies.json
with open('movies.json', 'w', encoding='utf-8') as f:
    json.dump(movies_data, f, ensure_ascii=False, indent=4)

print(f"Done! Scraped {len(movies_data)} CineSubz movies.")
