#! python3
# Healthgrades web scraping

import requests, bs4, json

session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

def makeRequest(url):
    global session
    res = session.get(url)
    try:
        res.raise_for_status()
    except Exception as err:
        print("ERROR: Failed to load page - " + str(err))
    return res

def soup(res):
    return bs4.BeautifulSoup(res.text, "html.parser")

def toJson(res):
    return json.loads(res.text)

def main():
    url = "https://silvercreekrealty.net/"

    webpage = soup(makeRequest(url))

    main()