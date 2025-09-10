# coding:utf-8
# author:杨淑娟
# 条件表达式只有if...else ，没有if ...elif ..else这种情况
a=eval(input('请输入a的值'))
b=eval(input('请输入b的值'))
x= a if a>b else b # 结果  a>b就把a的值赋给x，否则就把 b的值赋给x
print(x)

result= 'a大于b'  if a>b else 'b大于a'
print(result)

#如果有三种情况，大于，小于，等于  (多分支结构)，你可以使用嵌套
result2= 'a大于b' if a>b else ( 'b大于a' if b>a else '相等')
print(result2)



