import re

# 匹配电话号码
tel="13412585211"
res=re.match('1[3-9][0-9]{9}',tel)
try:
    print(res.group())
except AttributeError as e:
    print(e)
# 匹配Email
email="python123@163.com"
ret=re.match('\w+@[a-z0-9]+[.]com',email)
try:
    print(ret.group())
except AttributeError as e:
    print(e)

# 匹配身份证号码
id="110233335533158621"
ret_id=re.match('[0-9]{17}[0-9xX]',id)
try:
    print(ret_id.group())
except AttributeError as e:
    print(e)


