# coding:utf-8
# author:杨淑娟
class CPU(): # cpu
    pass

class Disk(): # 硬盘
    pass

class Computer():
    def __init__(self,cpu,disk): # 将cpu对象，disk对象作为参数
        self.cpu=cpu
        self.disk=disk

import copy
if __name__ == '__main__':

    cpu=CPU()                  # 创建了一个CPU对象，就是在内存中开了空间，具有id值
    disk=Disk()                # 同上
    computer=Computer(cpu,disk)  # 同上    # 17到19行代码，一共开了三个空间，具有三个id值 ，传对象值，传递 的是内存地址id值



    print('computer-id:',id(computer),'cpu-id',id(computer.cpu),'disk-id',id(computer.disk))

  # 浅拷贝3  （外变，里不变【里-->指的是传递过去的对象不变】）
    computer2=copy.copy(computer)  # 对computer对象进行浅拷贝 ，产生一个新的computer对象，但是不会产生新的cpu与disk对象
    print('computer2-id:',id(computer2),'cpu-id',id(computer2.cpu),'disk-id',id(computer2.disk))

    # 深拷贝 （外变，里也变）对computer对象进行深拷贝 ， 产生了一个新的computer对象，也产生了一个新的cpu对象和一个新的disk对象
    computer3 = copy.deepcopy(computer)
    print('computer3-id:', id(computer3), 'cpu-id', id(computer3.cpu), 'disk-id', id(computer3.disk))
