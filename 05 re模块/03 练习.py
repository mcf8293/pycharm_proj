import re
import urllib.parse

# text = '"url":"https:\/\/xhla.mjfkvt.com\/videos2\/e65e3d28ca01107b3692c1c18222a492\/e65e3d28ca01107b3692c1c18222a492.m3u8?auth_key=1696477751-651e3237783f1-0-ddbd509266e40425b16a504fdc114de5&v=3&time=0"'
# txt='"url":"https:\/\/vip8.3sybf.com\/20230924\/ELvNZ4xP\/index.m3u8"'
# url=re.findall(r'"url":"(.*?)"',text)[0].replace("\\","")
# url2=re.findall(r'"url":"(.*?)"',txt)[0].replace("\\","")
# text='18812345678,他还有一个电话号码是18887654321，他爱好的数字是0123567891，他的座机是：0571-52152166'
# res=re.findall(r'^1\d{10}|^\d{4}-\d{8}',text)
# text='<span>3896522</span>'
# result=re.findall(r'<span>(\d+)</span>',text)
# print(result)

html = """  
<link href="/static/css/style.css" rel="stylesheet" type="text/css" />  
<li><a href="/new/" class="nav-link" rel="nofollow">最新</a></li>   
<li><a href="/tupian/30511.html" target="_blank"><b>卿卿日常 田曦薇 6k无水</b></a></li>   
<li><a href="/tupian/30355.html" target="_blank"><b>坏蛋联盟 4k 壁纸</b></a></li>   
<li><a href="/tupian/29993.html" target="_blank"><b>苍兰诀 虞书欣古装剧照4</b></a></li>  
"""

result=re.findall('<li><a href="(.*?)".*?</b>',html)
print(result)


