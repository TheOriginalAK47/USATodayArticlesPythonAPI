import requests

class USATodayArticles:
    #def _init_(self):
    #    self.key = ''
    #    self.section = ''

    #def _init_(self, key):
    #    self.key = key
    #    self.section = ''

    def __init__(self, key, section):
        test = requests.get('http://api.usatoday.com/open/articles/topnews?api_key=' + key)
        if (test):
            self.key = key
        else:
            self.key = ''
        if (section == 'home'):
            self.section = ''
        else:
            self.section = section

    def isKeyValid():
        test = requests.get('http://api.usatoday.com/open/articles/topnews?     api_key=' + key)
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
