# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
# 直播做一个小项目
'''
1.Python的基础语法
2.流程控制
3.列表
4.面向对象

VIP 免费获取
Python常见问题100问  --》简称 Python100问
Python趣味编程100题  --》Python100题
Python函数大数        -->Python函数大全


'''
class Product(object):
    # 创建完对象，属性进行赋初始值
    def __init__(self,id,name,price,color,size,stock) -> None:
        self.id=id
        self.name=name
        self.price=price
        self.color=color
        self.size=size
        self.stock=stock

    #重写__str__方法之后，在创建对象之后，输出对象的名称时，将不再输出内存地址，输出的对象的属性值

    def __str__(self) -> str:
         # 10表示字符的显示宽度，<表示的是左对齐，如果实际宽度超过10，将使用实际值的宽度显示
        s='{0:<10}{1:<10}{2:<10}{3:<10}{4:<10}{5:<10}'  #采用的是格式化字符串
        return  s.format(self.id,self.name,self.price,self.color,self.size,self.stock)


class CartItem(object):

    def __init__(self,id,name,price,amount) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.amount=amount

    def __str__(self) -> str:
        s='{0:<10}{1:<10}{2:<10}{3:<10}'
        return s.format(self.id,self.name,self.price,self.amount)


product_lst=[]
cartitem_lst=[]  #购物车条目的列表
def add_cart_item(cartitem):
    flag=False
    for item in cartitem_lst:
        if item.id==cartitem.id:  #说明商品的已在购物车条目中存在
            flag=True
            item.amount+=cartitem.amount
            break
    if not  flag:
        cartitem_lst.append(cartitem)
    print('添加成功')


def inital():
    pro1 = Product(1111, '华为手机', 4999, '红色', 57, 10000)
    pro2 = Product(2222, '苹果手机', 9999, '蓝色', 67, 4000)
    pro3 = Product(3333, '小米手机', 3999, '金色', 37, 100)
    #将三个商品添加到列表中
    product_lst.append(pro1)
    product_lst.append(pro2)
    product_lst.append(pro3)

#添加商品的函数
def add_product(product):
    flag=False    # 表示要添加的商品在列表中不存在
    for item in product_lst:  #遍历列表
        if item.id==product.id:
            flag=True    #说明要添加的商品在列表中存在
            item.stock+=product.stock   # 商品不再添加，但是数量增加
            return
    if not flag:  #如果要添加的商品在列表中不存在，将商品添加到商品的列表中
        product_lst.append(product)

#根据编号查询商品
def find_by_id(id):
    for item in product_lst:
        if item.id==id:
            return item   #结束函数

def main_menu():
    while True:
        print('1.添加商品')
        print('2.查询所有商品')
        print('3.根据编号查询商品')
        print('4.添加商品进购物车')
        print('5.查看购物车')
        print('6.退出')
        choice=eval(input('请选择编号'))
        if choice==1:
            id=eval(input('请输入商品的ID'))
            name=input('请输入商品的名称')
            price=eval(input('请输入商品的价格'))
            color=input('请输入商品的颜色')
            size=eval(input('请输入商品的尺寸'))
            amount=eval(input('请输入商品上架数量'))
            pro=Product(id,name,price,color,size,amount) #创建商品对象
            #调用添加商品的函数
            add_product(pro)
        elif choice==2:
            for item in product_lst:
                print(item)
        elif choice==3:
            id =eval(input('请输入要查询的商品的id'))
            #调用函数
            product=find_by_id(id)
            if product!=None:
                print(product)
            else:
                print('对不起，您所查询的商品不存在')
        elif choice==4:
            id=eval(input('请输入商品中的id'))
            amount=eval(input('请输入购买数量'))
            product= find_by_id(id) #调用根据编号查询商品的函数查询要添加的商品
            if product!=None:
                cartitem=CartItem(id, product.name,product.price,amount)

                add_cart_item(cartitem)  #添进购物车
                product.stock-=amount  #减少库存
            else:
                print('对不起，您要添加进购物车的商品已下架')
        elif choice==5:
            for item in range(len( cartitem_lst)-1,-1,-1):
                print(cartitem_lst[item])
        elif choice==6:
            print('谢谢您的使用')
            break    #退出循环
if __name__ == '__main__':  #以主函数的形式运行
   inital()   #给列表进行赋值
   main_menu()


