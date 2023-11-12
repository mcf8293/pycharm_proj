"""
os.path模块在Python中提供了许多用于处理文件路径的函数。以下是一些常用的os.path函数及其用法：

1.os.path.abspath(path)：返回指定路径的绝对路径。

python
import os
path = "relative/path/to/file.txt"
absolute_path = os.path.abspath(path)
print(absolute_path)
2.os.path.join(path1[, path2[, ...]])：将多个路径组合成一个路径。

python
import os
path1 = "path/to"
path2 = "file.txt"
complete_path = os.path.join(path1, path2)
print(complete_path)
3.os.path.dirname(path)：返回指定路径的目录名。

python
import os
path = "/path/to/file.txt"
directory = os.path.dirname(path)
print(directory)
4.os.path.basename(path)：返回指定路径的文件名。

python
import os
path = "/path/to/file.txt"
filename = os.path.basename(path)
print(filename)
5.os.path.exists(path)：检查指定路径是否存在。

python
import os
path = "/path/to/file.txt"
if os.path.exists(path):
    print("File exists")
else:
    print("File does not exist")
6.os.path.isfile(path)：检查指定路径是否为文件。

python
import os
path = "/path/to/file.txt"
if os.path.isfile(path):
    print("Path is a file")
else:
    print("Path is not a file")
7.os.path.isdir(path)：检查指定路径是否为目录。

python
import os
path = "/path/to/directory"
if os.path.isdir(path):
    print("Path is a directory")
else:
    print("Path is not a directory")

"""
