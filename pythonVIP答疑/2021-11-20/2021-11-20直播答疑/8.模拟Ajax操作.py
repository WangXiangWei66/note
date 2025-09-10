# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
lst=['中华人民共和国','中华民族大团结','中国人','中国梦','中华香烟']
s=input('百度一搜你就知道:')
for item in lst:
    if item[:len(s)]==s: # item[:len(s)]切片操作
        print(item)
