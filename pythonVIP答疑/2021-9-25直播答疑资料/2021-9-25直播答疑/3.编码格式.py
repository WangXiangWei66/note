# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
#
# with open('a.txt','w') as file:  # 默认编码格为gbk
#     file.write('你好')

# 读取
with open('a.txt','r',encoding='gbk') as file: #这里的encoding='gbk'写与不写都行
    print(file.read())