import os

# 指定图片所在的目录
pic_dir = 'pic'
basepath=os.path.join(os.getcwd(), pic_dir)

# 获取目录下所有的文件和子目录
for filename in os.listdir(basepath):
    file_path = os.path.join(pic_dir, filename)

    # 如果是文件，直接删除
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"已删除文件: {file_path}")

    # 删除目录
os.rmdir(pic_dir)
print(f"已删除目录: {pic_dir}")