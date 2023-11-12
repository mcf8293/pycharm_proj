import os
import shutil

# 指定图片所在的目录
pic_dir = 'pic'

# 检查目录是否存在
if os.path.exists(pic_dir):
    # 递归删除目录及其内容
    shutil.rmtree(pic_dir)
    print(f"已删除目录: {pic_dir} 及其所有内容")
else:
    print(f"目录不存在: {pic_dir}")
