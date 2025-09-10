# coding:utf-8
# author:杨淑娟
import os.path
s=os.path.abspath('a.txt')
print(s) # 结果是一个字符串，
print(os.path.exists(s)) # 这才是判断 这个路径下的a.txt文件是否存在