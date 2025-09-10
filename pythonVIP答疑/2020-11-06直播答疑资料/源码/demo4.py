# coding:gbk  ，那么demo4.py文件的编码格式就是ANSI
# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
fp=open('a.txt','w')  #没有指定编码格式，，默认是gbk对应的是txt文件的ANSI码 ,
fp.write('中国你好') #一个中文占2个字节，所以 2*4

fp=open('b.txt','w',encoding='utf-8')  # 指定了utf-8的编码格式，所以一个中文占3个字节
fp.write('中国你好') #3*4   encoding 指定的是.txt文件的编码格式

'''Python文件的编码格式怎么指定？ 在python文件的最前头开始设置
  默认是什么？ utf-8'''



