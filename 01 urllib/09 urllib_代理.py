"""
配置代理：
1.创建Request对象
2.创建proxyHandler对象
3.用handler对象创建opener对象
4.使用opener.open函数发送请求
"""
import urllib.request
url="http://www.baidu.com/s?wd=ip"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
request=urllib.request.Request(url=url,headers=headers)
proxies={'http':'117.141.155.244:53281'}
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)