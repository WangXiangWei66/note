# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
#文件读取中的seek方法

with open('a.txt','w',encoding='utf-8') as file:
    file.write('中国你好！')
#a.txt由于编码格式为utf-8，所以每个中文占3个字节

#要进行文件读取
with  open('a.txt','r',encoding='utf-8') as file:
    file.seek(3) #跳过三个字节  （跳过一个汉字）   到底应该是 seek(2)还是seek(3)取决于编码式

    print(file.readline())