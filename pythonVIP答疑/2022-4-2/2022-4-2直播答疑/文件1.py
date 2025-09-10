# coding:utf-8
# author:杨淑娟

#需求：得到所有的质数,并打印1000以下的
#得到所有奇数(1除外)的生成器
def odd_num():
    a=1
    while True:
        a+=2
        yield a

def tt():
    yield 2
    b=odd_num()
    while True:
        i=next(b)

        b=filter(myfilter(i),b)   # 使用myfilter函数，过滤b
        yield i


def myfilter(n):

    return lambda x:x%n>0  #x是否一个奇数,n代表小于当前x的一个质数
#print(tt()) # 结果是一个生成器对象
# print(result)

for j in tt():
    if j<100:
        print(j)
    else:
        break