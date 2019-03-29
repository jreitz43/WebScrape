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

def getPayload():
    return {"requester.AccountID":"1838","requester.ApplicationProfile":"dsSearchAgentV3","directive.SortOrders[0].Column":"DateAdded","directive.SortOrders[0].Direction":"DESC","directive.ResultsPerPage":"250","responseDirective.IncludeMetadata":"true","query.SearchSetupID":"6069","query.LinkID":"-1","query.PriceMin":"200000","query.PriceMax":"400000","query.ImprovedSqFtMin":"1500","query.BathsMin":"2","query.ListingStatuses":"1","query.PhotoCountMin":"1","query.Counties[0]":"Ada","query.PropertyTypes[3]":"4719","query.PropertyTypes[2]":"4718","query.PropertyTypes[1]":"4716","query.PropertyTypes[0]":"4713","query.PropertyFeatures[0]":"6023"}

def search():
    global session
    url = "https://idx.diversesolutions.com"
    payload = getPayload()

    results = session.post(url, data=payload)
    print(results)

def main():
    search()

main()