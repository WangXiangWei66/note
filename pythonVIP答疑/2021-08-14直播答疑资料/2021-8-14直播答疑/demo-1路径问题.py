# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import os
#b=os.path.join('C:/','count_xstc') # 一个就够
#b=os.path.join(r'C:\','count_xstc') # 报错, 原字符的最后一个，不允许是一个\
b=os.path.join('C:\\','count_xstc')
print(b)

#str中的join方法
lst=['c:\\','count_xstc'] # 路径中的盘符是不区分大小写的
print(''.join(lst))
print('c:\\'+'count_xstc')
print('-----------------------------')

list1=os.listdir(b)
for item in list1:
    print(item)


# 路径是 字符串，字符串没有对与错  ，系统找不到指定的路径。 说明这个路径在磁盘上存在
# 路径是由字符串组成
# os.listdir(path) 获取path下的文件及文件夹
# os.walk(path) 获取path下的文件及子文件

lst2=os.walk(b)
# 文件夹路径  子文件夹名字列表  文件夹下的文件列表
for dirpath,dirnames,filenames in lst2:
    print(dirpath,dirnames,filenames )
    print('-----------------------------')
# scandir()查询文件/文件夹的信息 --（相当于查看文件及文件夹的属性,但是查看不了文件中的内容，
# 如果想查看文件中的内容用open()）
print('---------------------------------------------------------')
for item in os.scandir(b):
    print(item.stat())

#查看详细信息
import datetime
that_time=datetime.datetime.fromtimestamp(1628923924)
print(that_time)