#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import os
# listdir与walk()
# (1)listdir()查看指定路径下的文件夹和文件夹
print(os.listdir('a'))  # [aa.py, b]


# (2)walk()查看指定路径下的所有文件及文件夹（相当于执行了递归操作）
for dirpath,dirname,files in os.walk('a'):
    print(files)
    print(dirname) # 最后会出现两个[]，因为c里面没有文件也没有文件夹了



