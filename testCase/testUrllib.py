# -*- codeing = utf-8 -*-
import urllib.request

# 打开网页get方法
response = urllib.request.urlopen("http://www.baidu.com")
# 指定编码
response = response.read().decode('utf-8')
# print(response)

# 打开网址post方法 http://httpbin.org
import urllib.parse

try:
    data = bytes(urllib.parse.urlencode({"name": "liqian"}), encoding="utf-8")
    resp = urllib.request.urlopen("http://httpbin.org/post", data=data, timeout=4)
    # print(resp.read().decode("utf-8"))
except urllib.error.URLError as e:
    print(e)

resp1 = urllib.request.urlopen("http://www.baidu.com")
# 获取状态码
# print(resp1.status)
# 获取响应头
# print(resp1.getheaders())
# 获取单个响应头属性
# print(resp1.getheader("Expires"))

url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}
method = "POST"
data = bytes(urllib.parse.urlencode({"name": "liqian"}), encoding="utf-8")
# 构建请求对象
req = urllib.request.Request(url=url, headers=headers, method=method, data=data)
resp2 = urllib.request.urlopen(req)
print(resp2.read().decode("utf-8"))
