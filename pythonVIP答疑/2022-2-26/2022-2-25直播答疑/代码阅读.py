# coding:utf-8
# author:杨淑娟
b = int(input('输入任意正整数'))
mylist = []
def func(a):
    for i in range(2, a):
        if a % i == 0:
            mylist.append(str(i))
            a = a // i
            return func(a)
    mylist.append(str(a))
    if len(mylist) > 1:
       # print('{}能分解为{}'.format(b, mylist))
        print(f'{b}=','*'.join(mylist))
    else:
        print('{}是质数'.format(a))


func(b)

