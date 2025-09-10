# coding:utf-8
# author:杨淑娟
class Singleton(object): # 这就是一个普通的类
    _instance = None   # 对象名

    def __new__(cls, *args, **kwargs):  # 重写了父类 object中的__new__方法，用于去创建对象
        if cls._instance is None:   # 判断对象是否为None，对象为None说明该对象没有被创建
            cls._instance = object.__new__(cls, *args, **kwargs) # 没有被创建，就去创建
        return cls._instance   # 如果对象不为None，直接将该对象返回（不会创建新的对象)



if __name__ == '__main__':
    instance1 = Singleton()  # 创建对象
    instance2 = Singleton()
    instance3 = Singleton()

    # 打印出 3 个实例对象的内存地址，判断是否相同。
    print(id(instance1))   # 输出对象的内存地址
    print(id(instance2))
    print(id(instance3))