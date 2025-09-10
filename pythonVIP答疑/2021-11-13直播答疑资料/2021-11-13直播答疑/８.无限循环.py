# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

while True :
    a=eval(input('请输入'))
    b=input('运算符')
    c=eval(input('请输入'))
    if b=='+':
        print(a+c)
    else:
        print('输入错误')
        break
    # 退出无限循环的条件
    answer=input('继续吗？y/n')
    if answer!='y':
        break  # 退的就是 循环