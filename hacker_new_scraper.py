import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    url = "https://news.ycombinator.com"

    response = requests.get(url)
    
    if response.status_code!=200:
        print(f"Failed to fetch: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find_all("span", class_="titleline")

    print("Top 5 Hacker News Post Titles:")
    for i, title in enumerate(titles[:5], 1):
        link = title.find("a")
        if link:
            print(f"{i} . {link.text}")
        
    with open("hacker_news_titles.txt", "w", encoding="utf-8") as file:
        for title in titles:
            link = title.find("a")
            if link:
                file.write(f"{link.text}\n")


def main():
    print("Scraped Content")
    scrape_hacker_news()

if __name__ == "__main__":
    main()