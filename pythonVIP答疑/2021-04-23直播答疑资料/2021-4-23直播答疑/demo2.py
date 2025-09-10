# 教育机构：马士兵教育
# 讲    师：杨淑娟
#从键盘录入一个数　，判断这个数在列表中是否存在
lst=[12,34,45,56,4,87,98,67,89]
num=eval(input('请输入一个整数：')) #ｅｖａｌ去掉字符串左右的引号

#使用一个布尔型变量
flag=False  # 假设flag的值为False时，表示没有找到
for item in lst:
    if num==item:
        print('找到了')
        flag=True
        break
    # else:
    #    flag=False # 没找到的时候flag的值 一直是False

# 循环之后，判断flag的值，才能知道是否找到
if not flag:    # 相当于 flag==False
    print('没找到')
