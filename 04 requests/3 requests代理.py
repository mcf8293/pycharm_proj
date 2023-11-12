import requests

url="https://www.baidu.com/s?"
headers={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
}
data={
    'wd':'ip'
}
proxies={
    'http':"117.26.41.87:8888"
}
response=requests.get(url=url,params=data,headers=headers,proxies=proxies)
content=response.text
with open("baidu.html","w",encoding="utf-8") as f:
    f.write(content)