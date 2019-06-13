import urllib.request
from bs4 import BeautifulSoup

class Inspector:
    url = ""
    data = ""
    bs = ""
    def __init__(self,url):
        self.url=url
        self.data = urllib.request.urlopen(url)
        self.bs = BeautifulSoup(self.data,'html.parser')

    #Get All Of A Tag In Page
    def get_all(self,tag):
        return self.bs.find_all(tag)

    #Get Title Of The Page
    def get_title(self):
        return self.bs.title.text

    #Get A Good Style Of Page Source Code
    def get_source(self):
        return self.bs.prettify()

    #Get Everything In Code(In Html Tags){A List}
    def get_html_childs(self):
        return self.bs.children

    #get Everything In Body
    def get_body(self):
        html = list(self.bs.children)
        max = [0,0]
        for i in html:
            if len(i) > max[0]:
                max[0] = len(i)
                max[1] = html.index(i)
        if max != 0:
            html = html[max[1]]
            return list(html.children)
        else:
            return "Nothing!!!"

    #Get Text Of A Tag
    def get_text(self,tag,other=""):
        return self.bs.find_all(tag,other)[0].get_text()

    #Get Some Tag Into Another Tag
    def css_selector(self,string):
        return self.bs.select(string)
