# coding:utf-8
# author:杨淑娟
for n in range(2,3):  # 等于2，但是小于3的整数
    for x in range(2,n):   # range(2,n)  产生个[2,n)之间的整数，包含2但是不包含n，当前n的值为2 ，根本没有这样的x
        if n%x==0:
            print(n,'等于',x,'*,n//x')
            break
    else:
            print(n,'是质数')