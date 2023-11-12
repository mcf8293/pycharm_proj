import urllib.request

url = "https://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
# 封装Request对象
# 注意：因为参数顺序的问题，不能直接写url和headers，中间还有data 所以需要关键字传参
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen( request)
content = response.read().decode("utf-8")
print(content)
