# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#列表生成式
L=[[row[i] for row in  matrix] for i in range(4)]
print(L)

print('---------------------')

L = []  #存储咱们的数据
for i in range(4):

    l_row=[]
    for row in matrix:
        l_row.append(row[i])  # 获取二维列表中的元素的[1,5,9]
    L.append(l_row)#    L= [[1,5,9],[2,6,10]]

print(L) # 显示最终的结果，不需要重复



