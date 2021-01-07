'''
手动设置Cookies
1.Cookies会失效
2. 登录后的每一个请求，都需要带着cookie。不然响应结果与预期可能不一样。
'''

# 百格活动

import requests

# 没有登录时，返回的是登录的页面。
r = requests.get("https://www.bagevent.com/account/dashboard")
print(r.text)

#带上cookie，返回登录的页面
head = {
"Cookie": 'BAGSESSIONID=bf6ebec5-4c8d-416b-acce-2cc9cd6fbe2e; JSESSIONID=40D340FBC8073451C4072C8D0E5B765F; __asc=8a2144d6176cc166e5c4a5c2d4a; __auc=8a2144d6176cc166e5c4a5c2d4a; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1609741791; MEIQIA_TRACK_ID=1mapwMFuDHF7ujFCHcXKClcndNS; MEIQIA_VISIT_ID=1mapwQv7Y2sq7r213n1eOVUdV18; _ga=GA1.2.830211632.1609741800; _gid=GA1.2.1771188792.1609741800; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1609741801; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38'
}
r = requests.get("https://www.bagevent.com/account/dashboard",headers=head)
print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text