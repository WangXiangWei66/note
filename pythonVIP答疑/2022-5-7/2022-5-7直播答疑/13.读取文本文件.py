# coding:utf-8
# author:杨淑娟
import os
import math
size=os.path.getsize('mydoc.txt') # 获取文件中字节数的大小
print(size)

page=math.ceil(size/10)  # 分页每10个字节一页，一共分3页 ，26个字节应该放到3页中存
print(page)
file=open('mydoc.txt','rb')  # 按字节读取
for i in range(1,page+1):  # 遍历循环，会产生一个1到3之间的整数

    if size<10:             # 如果小于10，就从当前位置 读到最后
        x=file.read()
    else:
        x=file.read(10)      # 每次读10个字节
    size = size - 10         # 每读10个，总字节要减少10

    # 将读取的内容写进文件，文件命名规则 ，mydoc1.txt,mydoc2.txt....
    with open('mydoc'+str(i)+'.txt','wb') as filew: # 按字节写入
        filew.write(x)
file.close() # 关闭文件