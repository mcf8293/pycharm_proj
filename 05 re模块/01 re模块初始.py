import re
s='<div class="abc"><div>胡辣汤</div><div>饭团</div></div>'
# result=re.findall(r'<div>(.*?)</div>',s)
# print(result)
s="""
<div class="西游记"><span id='10010'>中国联通</span></div>
<div class="西游记"><span id='10086'>中国移动</span></div>
"""
result=re.findall(r"<span id='(\d+)'>(.*?)</span>",s)
print(result)