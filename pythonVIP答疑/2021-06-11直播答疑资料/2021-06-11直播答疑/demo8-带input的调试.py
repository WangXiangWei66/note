#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
year = [82, 89, 88, 86, 85, 00, 99]
print('原列表：', year)
for index, value in enumerate(year): # enumerate枚举 ，将列表中的索引和元素全都列举出来
       if str(value) != '0':
           year[index] = int('19' + str(value))
       else:
           year[index] = int('200' + str(value))
print('修改之后的列表：', year)
year.sort()
print('排序之后的列表为：', year)
#这题我的疑问就是这句的作用：for index, value in enumerate(year):
#第二题的：
lst = []
for i in range(0, 5):
    goods = input('请输入商品编码和商品名称进入商品的入库，每次只能输入一件商品：\n')
    lst.append(goods)
for item in lst:
    print(item)
cart = []
while True:
    num = input('请输入要购买的商品编号：')
    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break
    if num == 'quit':
         break
print ('您购物车里已经选好的商品为：')
for i in range(len(cart)-1, -1, -1):
    print(cart[i])
#这题我的疑问就是这句的作用：for i in range(len(cart)-1, -1, -1):
# len(cart)-1 --> start ，起始位置
# -1 --->stop  , 结束位置
# -  -->step  ,步长
# lst=[10,20,309,409]
#  for i in range(len(lst)-1,-1,-1)  结为  range(3,-1,-1 )  获得到的结果 [3,2,1,0]
#    print(lst[3])
#    print(lst[2])
#    print(lst[1])
#    print(lst[0])   # 元素的倒序输出
