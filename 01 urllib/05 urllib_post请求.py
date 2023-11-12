import urllib.request
import urllib.parse
import json
url='https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
data = {
    'kw': 'spider'
}
# post请求的参数必须要进行编码
params =urllib.parse.urlencode(data).encode('utf8')
# post请求的参数需要放在请求对象定制的参数中
request=urllib.request.Request(url=url, data=params, headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
str_json=json.loads(content)
print(str_json)