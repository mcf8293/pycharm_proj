from pprint import pprint

import requests
import re

url="https://www.gushiwen.cn/default_1.aspx"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
response=requests.get(url=url, headers=headers)
response.encoding="UTF8"
poeties=[]
titles=re.findall('<b>(.*?)</b>',response.text,re.DOTALL)
dynaties=re.findall('<p class="source">.*?<a.*?<a.*?>(.*?)</a>',response.text,re.DOTALL)
authors=re.findall('<p class="source">.*?<a.*?<img.*?>(.*?)</a>',response.text,re.DOTALL)
new_authors=[]
for author in authors:
    new_author=re.sub('\n',"",author)
    new_author=new_author.strip()
    new_authors.append(new_author)
contents=re.findall('<div class="contson".*?>(.*?)</div>',response.text,re.DOTALL)
new_contents=[]
for cont in contents:
    new_cont=re.sub('<.*?>','',cont).strip()
    new_contents.append(new_cont)
for title,dynasty,author,content in zip(titles,dynaties,new_authors,new_contents):
    poems={
        "title":title,
        "author": author,
        "dynasty":dynasty,
        "content":content
    }
    poeties.append(poems)
pprint(poeties)
