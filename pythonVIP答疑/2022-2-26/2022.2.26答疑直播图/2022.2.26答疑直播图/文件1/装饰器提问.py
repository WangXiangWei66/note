# coding:utf-8
# Author: Wu Xiaofeng
# Data: 2022/2/25 14:57
import time
def slow(seconds):
    def decorator_slow(func):
        def wrapper_slow(*args,**kwargs):
            print(f'{func.__name__} slepping {seconds} seconds')
            time.sleep(seconds)
            res=func(*args,**kwargs)
            return res
        return wrapper_slow
    return decorator_slow
@slow(3)
def add(a,b):
    print(a+b)
