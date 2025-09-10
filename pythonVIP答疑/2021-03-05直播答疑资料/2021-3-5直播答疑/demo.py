# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 图书管理系统的面向过程操作方式
lst=[]
def query():
    for book in lst:
        print(book)

def  add(book_name,book_id,book_author,book_price):
    lst.append([book_id,book_name,book_author,book_price])

def start():
    while True:
        print('-----------图书管理系统-------------')
        print('1.查询  2.添加   0.退出')
        choice=eval(input('请选择'))
        if choice==1:
            query()
        elif choice==2:
            add('Python程序设计',1001,'杨淑娟',90)
        elif choice==0:
            break
        else:
            print('对不起，没有选项请重新输入')

from bs4 import BeautifulSoup
from decimal import Decimal
# 一个.py结尾的文件 就是一个模块 ，
# 在模块中定义类  类使用class ，表示的是一种自定义数所据类型
# 模块中可以包含：函数，变量，语句，类。。
# 如查demo.py被导入到其它模块中，那么if中代码是不会被执行的
if __name__ == '__main__':
    start()

    s='hello'

