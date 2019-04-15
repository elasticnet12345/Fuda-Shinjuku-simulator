import requests
from bs4 import BeautifulSoup
# ===================================================-
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
        url = "https://transit.yahoo.co.jp/search/result?flatlon=&fromgid=&from=%E5%B8%83%E7%94%B0&tlatlon=&togid=&to=%E6%96%B0%E5%AE%BF&viacode=&via="
        if self.flag:
            # url += "&viacode=&via=&viacode=&via="
            url += "%E8%AA%BF%E5%B8%83&viacode=&via=&viacode=&via="
        url += "&y="+str(self.time["year"])
        url += "&m="+self.make_02d(self.time["month"])
        url += "&d="+self.make_02d(self.time["day"])
        url += "&hh="+str(self.time["hour"])
        self.split_minute()
        url += "&m2="+self.m2
        url += "&m1="+self.m1
        url += "&type=1&ticket=ic&expkind=1&ws=1&s=0&kw=%E6%96%B0%E5%AE%BF"
        # url = "https://transit.yahoo.co.jp/search/result?flatlon=&fromgid=&from=%E5%B8%83%E7%94%B0&tlatlon=&togid=&to=%E6%96%B0%E5%AE%BF&viacode=&via=&viacode=&via=&viacode=&via=&y="+str(self.time["year"])+"&m="+"&m="+self.make_02d(self.time["month"])+"&d="+self.make_02d(self.time["month"])+"&hh="+str(self.time["hour"])+"&m2="+self.m2+"&m1="+self.m1+"&type=1&ticket=ic&expkind=1&ws=1&s=0&kw=%E6%96%B0%E5%AE%BF"
        return url
    
    def research(self):
        """ 経路を検索する
        """
        # ===================================================-
        proxies = {
        'http':'http://proxy.uec.ac.jp:8080',
        'https':'http://proxy.uec.ac.jp:8080'
        }
        # ===================================================-
        url = self.get_url()        
        r = requests.get(url, proxies=proxies)         #requestsを使って、webから取得
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


        
