import requests

class USATodayArticles:
    def __init__(self):
        self.count = 10
        self.days = 0
        self.page = 0
        self.reporter = ''
        self.tickers = False

    def setKey(self, key):
        if (isKeyValid(key)):
            self.key = key
            return True
        else:
            return False

    def getArticles():
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


    def setCount(num):
        self.count = num

    def getCount():
        return self.count

    def setDays(num):
        self.days = num

    def getDays():
        return self.days

    def setPage(page):
        self.page = page

    def getPage():
        return self.page

    def setReporter(reporter):
        self.reporter = reporter

    def getReporter():
        return self.reporter

    def tickersOn():
        self.tickers = True

    def tickersOff():
        self.tickers = False

    def tickersStatus():
        return self.tickers

    def setEncoding(encoding):
        self.encoding = encoding

    def getEncoding():
        return self.encoding

def isKeyValid(key):
    print 'http://api.usatoday.com/open/articles/topnews?api_key=' + key
    test = requests.get('http://api.usatoday.com/open/articles/topnews?     api_key=' + key)
    print test
    if (test):
        return True
    else:
        return False
