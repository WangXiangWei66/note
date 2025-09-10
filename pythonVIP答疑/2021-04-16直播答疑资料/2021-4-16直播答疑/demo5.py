# 教育机构：马士兵教育
# 讲    师：杨淑娟

#输出三角形的规律　，外层控制行，内层控制列
N=eval(input('请输入行数'))
for i in range(1,N+1): #输出N 行
    for j in range(1,i+1):  # 个数，规则是行数与个数相同  ,包含i但不包含i+1
        if i==N:
            print('*', end='')
            # 空心三角形，使用判断
        else:
            if j==1 or j==i:

                print('*' ,end='')
            else:
                print(' ',end='')
    print() #换行

