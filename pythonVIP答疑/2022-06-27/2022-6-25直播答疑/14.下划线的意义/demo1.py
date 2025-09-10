# coding:utf-8
# author:杨淑娟
from bs4 import  BeautifulSoup
# (1)前置的单下划线 _var
class Test:
    def __init__(self):  # 特有方法
        self.foo=11    # 普通的成员变量
        self._bar=23    #   变量前加了一个下划线



if __name__ == '__main__':
    t=Test()
    print(t.foo)
    print(t._bar) # 可正常访问，但是会影响从模块导入名称的方



def external_func():  # 这是一个函数
    return 23

def _internal_func():  # 这也是一个函数，这个函数的名称前有一个下划线
    return  42


# (2)后置的单下划线 var_

# 当一个属性名恰好跟Python关键字重名，为了直观，可以在属性名后加_
bs=BeautifulSoup('<html><title>你好</title><body><div class="red">大家好</div><div>Python娟子姐</div></body></html>','lxml')
div=bs.find('div',class_='red')  # 后置的单下划线
print(div.text)


# (3)前置的双下划线__var (防止变量在子类中被覆盖），私有变量
class Test():
    def __init__(self):
        self.bar=11
        self._bar=23    # 半私有 （导入到其它文件时会出问题 ）
        self.__bar=42

t=Test()
print(dir(t))
print(t.bar,t._bar)#,t.__baz)
#print(t.__baz)
print(t._Test__bar)  # 这样去访问一个类的私有属性


# (4)前后置的双下划线__var__,Python中的特殊方法   __init__


# (5)单独的下划线 ： _, 用不到的变量使用_，如for
for  _ in range(10):
    print('helloworld')

