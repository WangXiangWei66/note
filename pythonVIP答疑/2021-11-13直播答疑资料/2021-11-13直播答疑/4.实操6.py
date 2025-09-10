# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
lst=[] # 用于存储商品信息
for i in range(5):
    goods=input('请输入商品信息，例如: 1001 手机')
    lst.append(goods)
# 考查的知识点是列表的创建与添加
print(lst)
# insert() 在指定位置添加，append()  在末尾处添加
#模拟用户购物
cart=[] # 代表购物车
while True:
    num=input('请输入您要购买的商品编号:')
    #使用遍历循环，判断要购买的商品是否在
    for item in lst: #每一个ｉｔｅｍ代表一种商品信息　1001 手机
        if item.find(num)!=-1: # 商品编号存在的情况
            cart.append(item) # 添加到购物车中
            print('商品已添回到购物车')
            break  # 退出for循环
    if num=='q':
        break  # 退出的while

#显示输出购物车商品信息
cart=cart[::-1] #列表的切片操作

for item in cart:
    print(item )

