# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

# 16.encoding，coding，decode之间的区别与应用
# coding ：用于设置python文件的编码格式，写入的位置，只能是python文件的第一行
# encoding: 方法的关键字参数,用于设置打开文件的编码格式
with open('a.txt','w',encoding='utf-8')as f : #a.txt文件的编码格式
    pass

# decode 是 bytes对象的方法， 用于解码
s='中国'
b=s.encode(encoding='utf-8') # 对s中的内容 中国 进行编码
print(b) #
# 解码
print(b.decode('utf-8'))
