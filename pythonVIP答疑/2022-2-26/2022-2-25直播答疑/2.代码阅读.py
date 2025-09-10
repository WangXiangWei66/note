# coding:utf-8
# author:杨淑娟
for n in range(2,3):  # range会产生一个大于等于2，小于3的整数  ，n的取值是2 ，只能是2
    for x in range(2,n): # range会产生一个大于等于2，小于n (n的值为2） 的整数，所以条件不成立,循环没执行
        if n%x==0:
            print(n,'等于',x,'*',n//x)
    else:                     # 执行的是else ,这个else是与内层for 一是组的为for ...else结构，
        print(n,'是质数')