# 判断是否存在download文件夹，如果没有就新建
import os

download_path=os.getcwd()+'\\download'
print(download_path)
if not os.path.exists(download_path):
    os.mkdir(download_path)
with open(download_path+"\\test.txt", "w",encoding="utf-8") as f:
    f.write("hello world")
