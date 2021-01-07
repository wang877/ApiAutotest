import requests
# url = "http://jy001:8081/futureloan/mvc/api/member/login"
url = "http://www.httpbin.org/post"
listes = [{"mobilephone":"15006007018","pwd":"","aa":"","bb":"login01"},
          {"mobilephone":"","pwd":"abc1234","aa":"abc1234","bb":"login02"},
          {"mobilephone":"","pwd":"","aa":"","bb":"login03"},
          {"mobilephone":"12345","pwd":"123456","aa":"123456","bb":"login04"}]
for listt in listes:
    r = requests.post(url,data=listt)
    print(listt["bb"])
    assert r.json()['form']['pwd'] == listt["aa"]

'''
url = "http://www.httpbin.org/post"
cs = {"mobilephone":"15006007018","pwd":""}
r=requests.post(url,data=cs)
print("++"+r.text)
assert "gzip, deflate" in r.text

cs = {"mobilephone":"","pwd":"abc1234"}
r=requests.post(url,data=cs)
print("=="+r.text)
assert r.json()['form']['pwd']=="abc1234"

cs = {"mobilephone":"","pwd":""}
r=requests.post(url,data=cs)
print("--"+r.text)
assert r.json()['form']['pwd']==""

cs = {"mobilephone":"12345","pwd":"123456"}
r = requests.post(url,data=cs)
print("000"+r.text)
assert r.json()['form']['pwd'] == "123456"
'''