import json

import requests

url="https://movie.douban.com/j/chart/top_list"
headers={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
}
# 重新封装参数
params={
"type": "24",
"interval_id": "100:90",
"action":"",
"start": "0",
"limit": "20",
}

resp=requests.get(url=url,params=params,headers=headers)
json_str=json.dumps(resp.json(),ensure_ascii=False)
with open("douban.json", "w",encoding="utf-8") as f:
    f.write(json_str)
    f.write("\n")
resp.close()
"""
get请求总结：
1.参数使用params传递
2.参数无需urlencode编码
3.不需要请求对象的定制
4，请求资源路径中的？可以加可以不加
"""
