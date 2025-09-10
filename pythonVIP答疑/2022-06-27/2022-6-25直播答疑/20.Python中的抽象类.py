# coding:utf-8
# author:杨淑娟
class Ali(object):  # 自定义的类   代表阿里支付
    def alipay(self):
        pass


class Ten(object):    # 自定义的类，表式的是腾讯支付
    def tenpay(self):
        pass


class App(object):    # 自定义的类，表示提苹果支付
    def apppay(self):
        pass

#都是一个支付，阿里的支付、腾讯的支付、苹果的支付方法名都不一样, 所带来的问题，调用非常的麻烦
# 使用if判断不同的类型，如果是Ali 支付则调用Ali的支付方法，如果是Ten支付，再支调用腾讯的支付方法，
# 再如果 App支付，就是调用APP的支付方法... 如果支付的方法更多，会加很多个if判断



# 解决方案 ，使用抽象类，  抽象类中只定义方法，不实现，由实现类去实现
from abc import ABCMeta
from abc import abstractmethod


# Payclass就是一个抽象类
class Payclass(metaclass=ABCMeta): # 是一个抽象类

    @abstractmethod   # 这就是一个装饰器，用来装饰pay这个方法的，说明这个pay方法是一个抽象方法
    def pay(self):
        pass            # 只需要占位即可，不需写代码


class Ali(Payclass):         # 阿里去继承支付类
    def pay(self, money):    # 重写父类的方法

        print("使用阿里支付{money}".format(money=money))


#

# 如果想使用抽象类，则只需要继承这个抽象类就可以了
class Ten(Payclass):          # 腾讯 去继承支付类
    def pay(self, money):   # 重写父类的方法
        print("使用微信支付{money}".format(money=money))


class App(Payclass):          # 苹果去继承支付类
    def pay(self, money):   # 重写父类的方法
        print("使用苹果支付{money}".format(money=money))



# 提取一个支付的函数    ,传入支付的对象，传入支付的金额即可
def pay(obj,money):
    obj.pay(money)

if __name__ == '__main__':
    # 根据传入的对象，调有相应对象的方法（不需要关注内部细节）
    pay(Ali(),1000)  # 调用 的是阿里的支付
    pay(Ten(),2000)  # 调用腾讯的支付
    pay(App(),3000) # 调用是苹果的支付

