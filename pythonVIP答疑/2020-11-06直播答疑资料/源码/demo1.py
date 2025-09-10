# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
print('hello') #默认输出到控制台上

'''def print(self, *args, sep=' ', end='\n', file=None):
           self  -->  创建对象的类的对象
           *args  -->个数可变位置参数
           end='\n'-->关键字参数（默认值参数），确定输出后的结束方式
           file=None--> 默认值为None ，指定数据的输出位置
           sep=' '-->分隔符号为空格

'''
print('hello','world','python')  # --》用到了*args  ，个数可变的位置参数
print('hello',end='\t')  #输出之后，以\t结尾 ，所以下行的world会在同一行中\t之后的位置输出
print('world')

fp=open('a.txt','w')   #会得到一个文件对象
print('hello',file=fp)

