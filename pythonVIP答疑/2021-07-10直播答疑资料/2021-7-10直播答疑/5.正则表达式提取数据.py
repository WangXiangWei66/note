#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import re
with open('发别人的处理文本.txt','r',encoding='gbk') as file:
    lst_txt=file.readlines()  # 读取全部数据结果为列表

#print(lst_txt)
for item in lst_txt:
    m=re.findall('=',item) # 查找所有等号的个数
   # print(m)
    if len(m)==1:
        print(item)
