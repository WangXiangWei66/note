# coding:utf-8
# author:杨淑娟
with open('stu.txt','r') as file:
    data=file.read()
    print(type(data))
    print(data)
    data=eval(data)  #
    print('-----------------------')
    print(dict(data))   # 这个dict不加也可以
    print(type(data))

    # 如果加上dict则表示为
    newdata=dict({'name':'marray','age':20})


#使用eval调用自定义函数

def fun():
    print('helloworld')

x=eval(input('请输入函数名'))

