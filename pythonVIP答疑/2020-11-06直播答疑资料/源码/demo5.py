# coding:gbk  ，那么demo4.py文件的编码格式就是ANSI
# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
'''如果不想手动close关闭系统资源 ，建议你使用上下文管理器with语句'''
with open('a.txt','w')as fp:  # 实际上as fp 相当于 fp=open(...)
    fp.write('中国你好') #

''' 为什么将fp称为上下文管理器对象？它又是怎么样关闭系统资源的呢？
    什么样的对象会被称为上下文管理器对象呢？
    如果一个类中实现了__enter__和__exit__方法，我们就称这个类对象遵守了上下文管理器协议 
    
'''
#print(dir(object))
class A (object):   #由于A这个类实现了__enter__和__exit__这两个特殊方法， 所以A就遵守了上下文管理器协议
    def __enter__(self):
        print('特殊方法__enter__被执行了')

        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('特殊方法__exit__被调用执行')

    def show(self): #A这个类的实例 方法
        print('helloworld')

#由于A是遵守上下文管理器协议的对象，所以创建A的对象可以采用上下管理器方法
#（1） 普通创建方式
a=A()
a.show()
print('---------------------------------------')
#(2)使用上下文管理器方式创建
with A() as a: #自动调用__enter__方法，进行上下文管理 器
    a.show()   #语句执行完毕，自动调用__exit__方法








