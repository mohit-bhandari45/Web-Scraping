import requests as rq

url = "https://timesofindia.indiatimes.com/technology/tech-tips/how-to-create-ghibli-style-anime-art-using-google-gemini-for-free/articleshow/119754131.cms"

def fetchUrlAndSaveToFile(url, path):
    r = rq.get(url)

    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)


fetchUrlAndSaveToFile(url, "data/times.html") 