# urllib.parseでGETのクエリが作成できる

import urllib.request
import urllib.parse

url = "https://transit.yahoo.co.jp/search/result"
params = {"from":"%E8%AA%BF%E5%B8%83&", "to":"%E6%96%B0%E5%AE%BF"}
encodeParams = urllib.parse.urlencode(params)
print(encodeParams)
print("=="*20)
with urllib.request.urlopen(url + "?" + encodeParams) as res:
    html = res.read().decode("utf-8")
    print(html)

