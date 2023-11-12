import urllib.request

url="http://www.baidu.com/"

#发送请求
resp=urllib.request.urlopen(url)

# 按照一个字节一个字节的去读
content=resp.read()
print(content)
# 返回多少个字节
content=resp.read(5)
print(content)
# 读取一行
content=resp.readline()
print(content)

content=resp.readlines()
print(content)
# 返回状态码，如果是200，证明逻辑没错
print(resp.getcode())
# 返回url
print(resp.geturl())
# 返回heads,一个状态信息
print(resp.getheaders())

