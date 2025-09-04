import requests
from bs4 import BeautifulSoup
from collections import Counter
import csv

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Error fetching: ", url)
        return None

def parse_headline(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    for item in soup.select('h2'):
        text = item.get_text(strip=True)
        if text:
            headlines.append(text)
    return headlines
    
def save_to_csv(headlines, filename="headlines.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["headline"])
        for h in headlines:
            writer.writerow([h])

def analyze_keywords(headlines):
    words = " ".join(headlines).lower().split()
    counter = Counter(words)
    return counter.most_common(10)

def main():
    url = "https://digiato.com/"
    html = fetch_page(url)

    if html:
        headlines = parse_headline(html)

        print(f"Collected {len(headlines)} headlines.")
        save_to_csv(headlines)

        top_words = analyze_keywords(headlines) 
        print("Top words: ", top_words)




if __name__ == "__main__":
    main()
