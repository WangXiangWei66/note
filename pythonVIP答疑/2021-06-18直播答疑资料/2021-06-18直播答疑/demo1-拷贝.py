# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
lst1=[10,[203,40],50]
#lst2=lst1[:]  # 切片操作 ，省略掉了 start :stop :step ,默认的是索引为0的位置 ，stop默认位置为len ,step默认为 1
lst2=lst1[0:len(lst1):1]
#　经过切片操作，就已经产生的浅拷贝的操作
print(id(lst1)) # 12288
print(id(lst2)) #12544
print('-----------------------------')
for i ,j in zip(lst1,lst2):
    print(id(i),id(j))




print('----------------------')
lst=[10,20,30]
print(id(lst)) #2355716737408
lst.clear()
print(id(lst)) #2355716737408
print('==============================')
lst=list(range(1,15))
print(lst)
dic={}
for i in range(3):
    dic[i]=lst
    print(id(dic[i]))
    lst.clear()
    print('------------------------',id(dic[i]))
print(dic)