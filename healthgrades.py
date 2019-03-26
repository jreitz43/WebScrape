#! python3
# Healthgrades web scraping

import requests, bs4, json

session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
session.headers['content-type'] = 'application/json; charset=UTF-8'
session.headers['x-requested-with'] = 'XMLHttpRequest'
session.headers['accept-encoding'] = 'gzip, deflate, br'
session.headers['accept-language'] = 'en-US,en;q=0.9'
session.headers['cache-control'] = 'no-cache'
session.headers['content-length'] = '26'
session.headers['pragma'] = 'no-cache'
session.headers['referer'] = 'https://icd10mappingtool.healthgrades.com/'
session.headers['origin'] = 'https://icd10mappingtool.healthgrades.com'

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

def getServiceLines():
    global session
    payload = {"pElement":"ServiceLine"}
    url = "https://icd10mappingtool.healthgrades.com/JSON.asmx/returnJSONforElement"

    servicelines = session.post(url, data=payload)
    print(servicelines)
    #servicelines = toJson(makeRequest(url))

    #print(servicelines['description'])

def main():
    url = "https://icd10mappingtool.healthgrades.com"

    webpage = soup(makeRequest(url))
    getServiceLines()

main()