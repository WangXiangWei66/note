#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
pwd=input('请输入密码:')# input()函数的结果要为str类型
print(type(pwd))
if pwd==8888: # 条件不成立， '8888'==8888 结果为False
    print(',,,,,,,,,,,')
else:
    print('===========================')
if pwd.isdigit(): # 判断密码是否是数字串
    print('密码合法')
else:
    print('密码只能是数字')


