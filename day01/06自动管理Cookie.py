'''
自动管理Cookie
requests中的Session类，能够自动获取和管理Cookie。
'''
import requests
# 新建一个session
s = requests.session()
print("登录之前的Cookie:", s.cookies)

# 登录接口 login
# 使用session发送请求
loginData={"access_type":"1",
          "loginType":"1",
          "emailLoginWay":"0",
           "account":"2780487875%40qq.com",
          "password":"qq2780487875",
          "remindmeBox":"on",
          "remindme":"1"}
r = s.post("https://www.bagevent.com/user/login", data=loginData)
# print(r.text)

print("登录之后的Cookie:", s.cookies)
# dashboard 接口
r = s.get("https://www.bagevent.com/account/dashboard")
# print(r.text)

# 退出登录 logout
r = s.get("https://www.bagevent.com/user/log_out")
# print(r.text)
print("退出登录之后的Cookie:", s.cookies)

# RequetsCookieJar转成字典
d = requests.utils.dict_from_cookiejar(s.cookies)
print(d)