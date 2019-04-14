import requests
from bs4 import BeautifulSoup

target_url = 'https://transit.yahoo.co.jp/search/result?flatlon=&fromgid=&from=%E5%B8%83%E7%94%B0&tlatlon=&togid=&to=%E6%96%B0%E5%AE%BF&viacode=&via=%E8%AA%BF%E5%B8%83&viacode=&via=&viacode=&via=&y=2019&m=04&d=14&hh=17&m2=4&m1=2&type=1&ticket=ic&expkind=1&ws=1&s=0&kw=%E6%96%B0%E5%AE%BF'
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

for li in soup.find_all('li',  attrs={"class": "time"}):
    #   print(span.get('href'))         #リンクを表示
    print(li.text)