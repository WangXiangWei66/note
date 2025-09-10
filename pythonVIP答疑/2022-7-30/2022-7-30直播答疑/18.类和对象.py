# coding:utf-8
# author:杨淑娟
# 比如说我想创建一本关于图书的类
# 编写类
class  Book():
    # 书的属性写在init中
    def __init__(self,name,author,publish,pubdate):
        self.name=name
        self.author=author
        self.publish=publish
        self.pubdate=pubdate  # 左边是实例属性，右边是局部变量
        # 如果左侧不写self. 在这个类的其它方法里是不可以使用
        a=100  # 因为这个a是__init__中的局部变量，只能在__init__方法中使用

    def show(self):
        print(self.name,self.author,self.publish,self.pubdate)
        #print(a) # 使用a的时候报错


if __name__ == '__main__':
    # 创建对象
   b1=Book('Python实战','PythonJuan','XXX出版社','2022-10-10')

   b2=Book('Python测试','Yang','YYYY出版社','2023-1-2')

   # b1和b2称为Book类的对象
    # 创建完对象，就可以调用方法
   b1.show()
   b2.show()