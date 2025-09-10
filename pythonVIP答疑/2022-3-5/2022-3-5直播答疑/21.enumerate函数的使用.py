# coding:utf-8
# author:杨淑娟
lst=['hello','world','Python','html','sql']
for index,item in enumerate(lst,11): # 遍历列表中的元素，并为元素指定序号从几开始，序号不指定，默认从0开始
    print(index,item)