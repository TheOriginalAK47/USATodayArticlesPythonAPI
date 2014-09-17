import requests

class ArticlesAPI:
    def __init__(self):
        self.count = 10
        self.days = 0
        self.page = 0
        self.reporter = ''
        self.tickers = False
        self.section = ''

    def setKey(self, key):
        if (isKeyValid(key)):
            self.key = key
            return True
        else:
            return False

    def getArticles(self):
        if not isKeyValid(self.key):
            return None
        requestURL = "http://api.usatoday.com/open/articles/topnews"
        if (self.section != ''):
            requestURL += '/' + self.section
        requestURL += "?"
        if (self.getCount() != 10):
            requestURL += str(self.getCount()) + '&'
        if (self.getDays() != 0):
            requestURL += str(self.getDays()) + '&'
        if (self.getPage() != 0):
            requestURL += str(self.getPage()) + '&'
        if (self.getReporter() != ''):
            requestURL += str(self.getReporter()) + '&'
        if (self.tickersStatus() == True):
            requestURL += 'Y' + '&'
        requestURL += self.key
        response = requests.get(requestURL)
        print response.text


    def setCount(self, num):
        self.count = num

    def getCount(self):
        return self.count

    def setDays(self, num):
        self.days = num

    def getDays(self):
        return self.days

    def setPage(self, page):
        self.page = page

    def getPage(self):
        return self.page

    def setReporter(self, reporter):
        self.reporter = reporter

    def getReporter(self):
        return self.reporter

    def tickersOn(self):
        self.tickers = True

    def tickersOff(self):
        self.tickers = False

    def tickersStatus(self):
        return self.tickers

    def setEncoding(self, encoding):
        self.encoding = encoding

    def getEncoding(self):
        return self.encoding

def isKeyValid(key):
    url = 'http://api.usatoday.com/open/articles/topnews?api_key=' + key
    print url
    test = requests.get(url)
    if (test):
        return True
    else:
        return False
