#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/3/11 17:49
#任务2：京东购物流程

#存放输入的商品信息
lst=[]
for i in range(5):
    good=input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品\n')
    lst.append(good)
#输出所有商品信息
for item in lst:
    print(item)

#存放购物车中的商品信息
cart=[]
while True:
    print('请输入要购买的商品的编号:' )
    num=input('')
    for item in lst:
        if item.find(num)==0:
            cart.append(item)
            print('商品已添加到购物车，请继续添加要购买的商品编号:')
            break
    if num=='q':
        break
print('您购物车里已经选择商品为:')

for m in cart:
    print(m)
