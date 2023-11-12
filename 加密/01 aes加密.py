import base64
from Crypto.Random import get_random_bytes
"""
#AES加密环境
#先卸载这些包，防止一些环境问题
pip uninstall crypto
pip uninstall pycryptodome
#在安装
pip install pycryptodome
如果出现报错：不存在Crypto，那么需要进入python包目录修改crypto为Crypto即可
路径：Python311\Lib\site-packages\
"""
from Crypto.Cipher import AES



# 将原始的明文用空格填充到16字节
'''
AES的区块固定是128比特，也就是16字节，
所以一开始要先判断明文是否小于16字节，
如果小于16字节，需要补齐，为此要写一个补齐的函数。
'''


def pad(data):
    pad_data = data
    for i in range(0, 16 - len(data)):
        pad_data = pad_data + ' '
    return pad_data


'''
步骤：
1.创建AES加密对象
2.用创建好的加密对象，对明文进行加密
3.把加密好的密文用base64编码
4.把字符串解码成字符串
'''


# 将明文用AES加密
def AES_en(key, data):
    # 将长度不足16字节的字符串补齐
    if len(data) < 16:
        data = pad(data)
    # 创建加密对象
    AES_obj = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    # 完成加密
    AES_en_str = AES_obj.encrypt(data.encode("utf-8"))
    # 用base64编码一下
    AES_en_str = base64.b64encode(AES_en_str)
    # 最后将密文转化成字符串
    AES_en_str = AES_en_str.decode("utf-8")
    return AES_en_str


'''
将密文解密
解密是加密的逆过程，按着加密代码的逆序很容易就能写出

将密文字符串重新编码成bytes类型
将base64编码解开
创建AES解密对象
用解密对象对密文解密
将补齐的空格用strip（）函数除去
将明文解码成字符串
'''


def AES_de(key, data):
    # 解密过程逆着加密过程写
    # 将密文字符串重新编码成二进制形式
    data = data.encode("utf-8")
    # 将base64的编码解开
    data = base64.b64decode(data)
    # 创建解密对象
    AES_de_obj = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    # 完成解密
    AES_de_str = AES_de_obj.decrypt(data)
    # 去掉补上的空格
    AES_de_str = AES_de_str.strip()
    # 对明文解码
    AES_de_str = AES_de_str.decode("utf-8")
    return AES_de_str

# 加密数据如果是中文，需要转码
def chinese_to_ascii(text):
    text2 = base64.b64encode(text.encode('utf-8')).decode('ascii')
    return text2

if __name__ == '__main__':
    # 定义好全局变量
    iv = 'aaaaccsdfaaafa12'  # iv是初始化向量,此处16|24|32个字符,分别对应AES-128、AES-192和AES-256
    key = 'miyaoxuyao16ziji'  # key是密钥，这里选择的长度是128比特，所以字符串的长度要固定在16
    nick = '你好'  # 需要加密的数据
    data=chinese_to_ascii(nick)
    data = AES_en(key, data)
    print(data)
    data = AES_de(key, data)
    print(data)
