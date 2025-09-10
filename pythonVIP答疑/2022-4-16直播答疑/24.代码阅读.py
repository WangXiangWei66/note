# coding:utf-8
# author:杨淑娟
def odd_num():
    n=1
    while 1:
        n+=2
        yield n

def my_filter(x):
    # return lambda y:y%x>0
    def odd(y):
        return y%x>0
    return odd

def all():
    yield 2
    g=odd_num()
    while True:
        num=next(g)
        g=filter(my_filter(num),g)
        #g=filter(lambda x:x%num>0,g)
        yield num
iter1=all()
for i in range(10):
    num=next(iter1)
    print(num)


