"""
安装requests:
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 04 requests
response的属性和类型
类型
response.text  获取网站源码
response.encoding 访问或定制编码方式
response.url     获取请求的url
response.content  响应的字节类型
response.status_code 响应的状态码
response.headers  响应的头信息
"""
import requests
url="https://fanyi.baidu.com/sug"
str=input("请输入你要翻译的英文单词:")
data={"kw": str}
# 发送post请求,发送的数据必须放在字典中
resp=requests.post(url=url, data=data)
print(resp.json())

"""
post请求总结：
1.参数使用data传递
2.参数无需urlencode编码
3.不需要请求对象的定制
4，请求资源路径中的？可以加可以不加
"""