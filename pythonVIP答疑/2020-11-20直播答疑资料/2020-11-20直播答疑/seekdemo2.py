# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
#文件读取中的seek方法

with open('b.txt','w',encoding='gbk') as file:
    file.write('中国你好！')   #总共占10个字节  2*5


# #要进行文件读取
with  open('b.txt','r',encoding='gbk') as file:
    file.seek(2)

    print(file.readline())