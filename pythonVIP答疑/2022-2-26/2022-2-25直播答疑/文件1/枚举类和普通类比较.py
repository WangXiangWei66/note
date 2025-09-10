# coding:utf-8
# Author: Wu Xiaofeng
# Data: 2022/2/25 15:35
from enum import Enum
class Color(Enum): # 第二种：自定义一个枚举类
    red = 100
    green =200
    blue =30
    yellow =200

    def a(self):# 不允许key相同或者value。
        pass
print(Color.blue)


class P():  # 默认继承object类
    pass
class P1(P):
    red=100
print(P1.red)

print(type(Color.blue))
print(type(P1.red))