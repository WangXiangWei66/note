# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class Site:
    def __init__(self,name,url):
        self.name=name
        self.__url=url
    def who(self):
        print('name:',self.name)
        print('url:',self.__url)
    def __foo(self):
        print('1')
    def foo(self):
        print('2')
        self.__foo()

x=Site('msb','www.mashibing.com')
x.who()
x.foo()
x.__foo()
