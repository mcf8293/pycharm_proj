import urllib.request

# 将中文变成unicode编码的格式
name = urllib.parse.quote('周杰伦')
print(name)
url = f"https://www.baidu.com?{name}"
url_err = "https://www.baidu.com?周杰伦"  # UnicodeEncodeError: 'ascii' codec can't encode characters in position 6-8: ordinal not in range(128)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
# 封装Request对象
# 注意：因为参数顺序的问题，不能直接写url和headers，中间还有data 所以需要关键字传参

# 1.请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 2.模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 3.获取响应的内容
content = response.read().decode("utf-8")
print(content)
