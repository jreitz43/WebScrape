#! python3
# Healthgrades web scraping

import requests, bs4, json

session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
session.headers['content-type'] = 'application/json; charset=UTF-8'
session.headers['Accept'] = 'text/javascript, text/html, application/xml, text/xml, */*'
session.headers['accept-encoding'] = 'gzip, deflate, br'
session.headers['accept-language'] = 'en-US,en;q=0.9'
session.headers['cache-control'] = 'no-cache'
session.headers['connection'] = 'keep-alive'
session.headers['content-length'] = '542'
session.headers['pragma'] = 'no-cache'
session.headers['referer'] = 'https://idx.diversesolutions.com/search/1838/6069?&oref=https%3A%2F%2Fsilvercreekrealty.net%2F'
session.headers['host'] = 'idx.diversesolutions.com'
session.headers['X-Prototype-Version'] = '1.7'
session.headers['X-Requested-With'] = 'XMLHttpRequest'
session.headers['origin'] = 'https://idx.diversesolutions.com'

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