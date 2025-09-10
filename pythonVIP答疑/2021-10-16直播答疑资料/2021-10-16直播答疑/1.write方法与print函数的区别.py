# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
lst=[
    {'name':'张三','age':20,'gender':'男'},
     {'name':'张三1','age':21,'gender':'男'},
    {'name':'张三2','age':22,'gender':'男'}
]
#使用print()内置函数
for item in lst:
    print(item,type(item))  # item类型都是字典类型
for item in lst:
    print(str(item),type(str(item))) #类型是字符串类型

#将列表中的数据写进文件
with open('a.txt','w',encoding='utf-8') as file:
    for item in lst:
        #file.write(item) #TypeError: write() argument must be str, not dict
        file.write(str(item)) # write()方法的参数必须是str类型

# w-->write  ，写入
# a-->append  ,追加写入
# wb -->write byte，写二进制