# coding:utf-8
# author:杨淑娟
# a-->追加写模式
# a+-->读写模式
file=open('a.txt','a+')
file.write('world')

print(file.read())

file.close()