import requests

class USATodayArticles:
    def __init__(self):
        self.key = ''
        self.section = ''

    def __init__(self, key):
        self.key = key
        self.section = ''

    def __init__(self, key, section):
        self.key = key
        if (section == 'home'):
            self.section = ''
        else:
            self.section = section

    def setAPIKey(key):
        test = requests.get('http://api.usatoday.com/open/articles/topnews?api_key=' + key)
        if (test):
            return True
        else:
            return False

    def getArticlesWithTag(tag):
        print(self.APICall())


    def APICall():
        return requests.get('http://api.usatoday.com/open/articles/topnews?api_key' + self.getAPIKey())


#def runTest():
#    print "Test ran."
