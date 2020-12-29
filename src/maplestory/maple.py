from bs4 import BeautifulSoup

import requests

starting_url = "https://maplestory.nexon.net/news/update#news-filter"

url_request = requests.get(starting_url)
url_text = url_request.text
soup = BeautifulSoup(url_text, "html.parser")

def get_latest_maple_news():
    maple_news_html = soup.find("li", attrs = {"class" : "news-item news-item--update"})

    maple_news_container = []

    for urls in maple_news_html.find_all("a", href = True):
        maple_news_container.append(urls["href"])

    half_url = "https://maplestory.nexon.net"

    full_url = half_url + maple_news_container[0]

    return full_url

if __name__ == "__main__":
    # parent = soup.find("li", attrs={"class": "news-item news-item--update"})

    # teoi = []

    # for item in parent.find_all("a", href=True):
    #     # print (item["href"])
    #     teoi.append(item["href"])

    # print (teoi[0])
    # # print (parent)

    get_latest_maple_news()