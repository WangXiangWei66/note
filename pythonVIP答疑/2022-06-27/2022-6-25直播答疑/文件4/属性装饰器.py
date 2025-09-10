# coding:utf-8
# author:杨淑娟
class Rect:    # 自定义的一个类
    def __init__(self,area):  # 初始化属性
        self.__area = area   # 使用了两个前置下划线，说明这个变量是“私有的”，在类的外部就不能使用


    @property                    # 装饰器，装饰 area这个方法的, 成为一个只读变量,无法修改该变量的值
    def area(self):
        return self.__area


    #而要想实现修改 area 属性的值，还需要为 area 属性添加 setter 方法，就需要用到 setter 装饰器，它的语法格式如下：
    @area.setter            # 又使用了一个装饰器叫setter，声明为可赋值的方法
    def area(self,value):
        self.__area=value


rect = Rect(30)
#直接通过方法名来访问 area 方法
print("矩形的面积是：",rect.area)   # 可以访问到了area这个变量的值
# 但是可以修改吗？
#rect.area=100
#可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。
#使用 ＠property 修饰了 area() 方法，这样就使得该方法变成了 area 属性的 getter 方法。需要注意的是，如果类中只包含该方法，那么 area 属性将是一个只读属性。

#rect.area=100
rect.area=100  # 可赋值
print(rect.area) # 可取值   ，area  可以加括号吗？ 不可以，因为有装饰器进行了装饰，所以不可以

