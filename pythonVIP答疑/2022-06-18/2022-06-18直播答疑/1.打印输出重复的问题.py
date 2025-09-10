# coding:utf-8
# author:杨淑娟
lst=['1001','1002']      #列表
stuno=input('输入学生的学号:') # 键 盘录入
for item in lst:   # 循环遍历 (遍历列表中的元素)
    if item==stuno:    #
        print('找到了')
        break
else:         # 让它成为   for....else结构  ,当在循环中没有遇到break时，就会执行else中的内容
        print(f'没找到学号为{stuno}的学生')
