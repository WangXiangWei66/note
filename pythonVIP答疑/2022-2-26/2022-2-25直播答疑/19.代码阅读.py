# coding:utf-8
# author:杨淑娟
number=int(input("请输入一个数字："))
newnum=number
new=[]
num=2
while num < newnum:
    if newnum % num ==0:
        newnum /= num
        new.append(str(num))
    num+=1
    #new.append(str(int(newnum)))
    new.sort()
print(str(number)+"="+"*".join(new))