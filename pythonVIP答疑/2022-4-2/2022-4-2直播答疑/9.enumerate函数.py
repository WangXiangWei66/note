# coding:utf-8
# author:杨淑娟
lst=[11,22,33,44,55]
# index表示的是序号， item表示的是lst列表中的元素
for index ,item in enumerate(lst,1): # enumerate自带一个序号，默认从0开始
    print(index,item)
