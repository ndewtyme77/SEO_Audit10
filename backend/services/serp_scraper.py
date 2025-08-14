import requests
from bs4 import BeautifulSoup

def get_keywords(url: str):
    domain = url.split("//")[-1].split("/")[0]
    query = f"site:{domain}"
    google_url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(google_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    titles = [t.get_text() for t in soup.select("h3")]
    words = {}
    for title in titles:
        for word in title.split():
            word = word.lower()
            if len(word) > 3:
                words[word] = words.get(word, 0) + 1
    sorted_keywords = sorted(words.items(), key=lambda x: x[1], reverse=True)
    return [k for k, _ in sorted_keywords[:10]]
