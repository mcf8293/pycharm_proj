import urllib.parse
import urllib.request

base_url = 'https://www.baidu.com/s?'
data = {
    'wd': '周杰伦',
    'sex': '男'
}
new_data = urllib.parse.urlencode(data)
# 请求资源的路径
url = base_url + new_data
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)
