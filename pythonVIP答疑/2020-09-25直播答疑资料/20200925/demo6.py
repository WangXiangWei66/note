#教育机构 ：马士兵教育
#讲    师：杨淑娟
fp=open('D:\\text.txt','a+',encoding='utf-8')  #内置函数open()打开磁盘文件，r表示的是read只读方法
                                         # w 表示的是write只写方法
                                         # a+ 读写方式打开

print('helloworld','Python',sep='*',file=fp)       # file 称为关键字参数 ,helloworld称为位置参数，

#helloworld和Python称为位置参数，   file称为关键字参数默认值为None
fp.close() # 对象的关闭方法


