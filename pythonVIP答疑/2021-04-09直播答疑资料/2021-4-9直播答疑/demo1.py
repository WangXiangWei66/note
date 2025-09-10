# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

file=open('c.txt','w')
file.write('你好啊')
file.close()
'''
demo1.py文件的编码格式为utf-8  ,第一种代码# coding:utf-8决定
c.txt文本文件的编码格式为gbk, 使用代码的方式创建的文本文件编码格式默认为GbK

'''

file=open('d.txt','w',encoding='utf-8') # 设置d.txt文本文件的编码格式
file.write('你好啊')
file.close()
