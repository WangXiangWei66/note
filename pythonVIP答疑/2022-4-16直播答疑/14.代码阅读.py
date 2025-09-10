# coding:utf-8
# author:杨淑娟
for n in range(2, 3):
    for x in range(2, n):
        if n % x == 0:
             print(n, '等于', x, '*,n//x')
             break
    else:
            print(n,'是质数')

