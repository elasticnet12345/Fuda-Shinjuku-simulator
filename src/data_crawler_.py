import requests
from bs4 import BeautifulSoup
import urllib



class TimeResearcher(object):
    """ 
    """
    def __init__(self, flag, time):
        """ 
            input: flag: 調布駅経由の有無
                   time: {"year", "month", "day", "hour", "minute"}
        """
        self.flag = flag
        self.time = time
        self.m1, self.m2 = None, None
        self.url = None

    def make_02d(self, num):
        """ 数字を2桁の数字の文字列にする
        """
        return "%02d"%(num)
    
    def split_minute(self):
        """ query が分を桁毎に分割していたので
        """
        minute = self.time["minute"]
        tmp = self.make_02d(minute)
        m1, m2 = tmp[0], tmp[1]
        self.m1 = m1
        self.m2 = m2
        
    def get_url(self):
        """ timeとflagを下に検索する
        """
        # url = "https://transit.yahoo.co.jp/search/result?flatlon=&fromgid=&from=%E5%B8%83%E7%94%B0&tlatlon=&togid=&to=%E6%96%B0%E5%AE%BF&viacode=&via="
        url = "https://transit.yahoo.co.jp/search/result?flatlon=&fromgid=&from=%E8%B6%B3%E6%9F%84&tlatlon=%2C%2C23209&togid=&to=%E6%96%B0%E6%9D%BE%E7%94%B0&viacode=&via="

        if self.flag:
            # url += "%E8%AA%BF%E5%B8%83&viacode=&via=&viacode=&via="
            url += "%E8%9E%A2%E7%94%B0&viacode=&via=&viacode=&via="
        else:
            # url += ""
            url += "%E5%B0%8F%E7%94%B0%E5%8E%9F&viacode=&via="
        url += "&y="+str(self.time["year"])
        url += "&m="+self.make_02d(self.time["month"])
        url += "&d="+self.make_02d(self.time["day"])
        url += "&hh="+str(self.time["hour"])
        self.split_minute()
        url += "&m2="+self.m2
        url += "&m1="+self.m1
        # url += "&type=1&ticket=ic&expkind=1&ws=1&s=0&kw=%E6%96%B0%E5%AE%BF"
        url += "&type=1&ticket=ic&expkind=1&ws=1&s=0&kw=%E6%96%B0%E6%9D%BE%E7%94%B0" # 目的地
        return url
    
    def research(self):
        """ 経路を検索する
        """
        # ===================================================-
        # proxies = {
        # 'http':'http://proxy.uec.ac.jp:8080',
        # 'https':'http://proxy.uec.ac.jp:8080'
        # }
        # ===================================================-
        url = self.get_url()        
        # r = requests.get(url, proxies=proxies)         #requestsを使って、webから取得
        r = requests.get(url)
        htmlSource = BeautifulSoup(r.text, 'lxml') #要素を抽出
        res_ = []
        for li in htmlSource.find_all('li',  attrs={"class": "time"}):
            res_.append(li.text)
        return res_

    
    def get_first_line(self):
        """ 複数の候補から最短を返す
        """
        lines_ = self.research()
        return lines_        


def main():
    # 時刻検索オブジェクト
    flag = False
    time = {"year":2019, "month":4, "day":15, "hour":8, "minute":32}
    time_researcher = TimeResearcher(flag, time)
    time_researcher.research()
    res = time_researcher.get_first_line()
    print("res:", res)


if __name__ == "__main__":
    main()


        
