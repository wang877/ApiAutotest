'''
1. 增加异常处理
2. 新建一个session，使用session发送请求，自动管理cookie
'''
import requests


class BaseRequests:
    def __init__(self):
        self.session = requests.session()

    def get(self,url, **kwargs):
        try:
            r = self.session.get(url, **kwargs)
            print(f"发送get请求, url : {url},请求参数:{kwargs}成功。")
            return r
        except Exception as e:
            print(f"发送get请求, url : {url},请求参数:{kwargs}异常,异常信息为:{e}。")

    def post(self, url, data=None, json=None, **kwargs):
        try:
            r = self.session.post(url, data=data, json=json, **kwargs)
            print(f"发送post请求, url : {url},请求参数:data:{data}, json:{json}, 其他：{kwargs}成功。")
            return r
        except Exception as e:
            print(f"发送post请求, url : {url},请求参数:data:{data}, json:{json}, 其他：{kwargs}异常,异常信息为:{e}。")

if __name__ == '__main__':
    r = BaseRequests().get("http://www.httpbin.org/get?name=root")
    print(r.text)
    cs = {"user":"root", "pwd":123456}
    r = BaseRequests().post("http://www.httpbin.org/post",data=cs)
    print(r.text)





