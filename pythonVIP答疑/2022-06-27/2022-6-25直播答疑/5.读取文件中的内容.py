# coding:utf-8
# author:杨淑娟
with open('b.txt','r',encoding='utf-8')as file:
    s=file.read()
    print(type(s),s)

    d=eval(s)  # 类型转换，将字符串转成了字典类型
    print(type(d),d)


with open('c.txt','r',encoding='utf-8')as file:
    s=file.read()
    print(type(s),s)
    lst=eval(s)
    print(type(lst),lst)
    ss=str(lst)                 # 将列表转成了字符串类型
    print(type(ss),ss)

