import os
import shutil

# 判断文件是否存在
print(os.path.exists('D:\\Code'))
# 判断路径是否为目录
print(os.path.isdir('D:\\Code'))
# 返回当前py文件路径
print(os.getcwd())
# 返回指定文件的绝对路径
print(os.path.abspath('test.py'))
# 读文件
file = os.getcwd()
f = open(file + '\\文件操作.py', encoding='UTF-8')
read_str = f.read()
f.close()
print(read_str)
# 写文件 mod:r(读)、w(写)、a(追加写入)
with open(file + '\\writer.txt', mode='a', encoding='utf-8') as ff:
    ff.write('我是被写入的字\n')
    ff.write('我再次被写入')
# 移动文件
shutil.move(os.path.abspath('writer.txt'), os.path.abspath('new_writer.txt'))
