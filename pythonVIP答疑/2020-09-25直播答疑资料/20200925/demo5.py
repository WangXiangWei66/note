#教育机构 ：马士兵教育
#讲    师：杨淑娟
#讲讲zip()
s='hello'
lst=[11,22,33,44]
lst2=['apple','orange','banana']
for   a,b,c in zip(s,lst,lst2):  #s是字符串类型，字符串是一个可迭代对象, lst是一个列表， 将
    #a表示的是字符串中遍历出来的内容 ,b表示的是列表中遍历出来的内容
    print(a,'---',b,'---',c)

