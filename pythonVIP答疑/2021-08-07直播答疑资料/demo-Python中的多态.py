#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class A:
    def show(self):
        print('A中的show方法')

class B:
    def show(self):
        print('B中的show方法')


def fun(obj): # 请问这个obj对象是谁？
    obj.show()
#　Python是一门动态语言,可以在创建对象后,动态的绑定属性和方法,动态语言崇尚的是"鸭子类型"
#当一只鸟走过来，这个鸟走起来像鸭子，游泳起来也像鸭子，叫起来也像鸭子，这个鸟就可以称为鸭子
fun(A())
fun(B())
