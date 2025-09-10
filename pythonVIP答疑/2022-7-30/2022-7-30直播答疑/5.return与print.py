# coding:utf-8
# uthor:杨淑娟
#(1)return使用的位置 是函数（方法）
#(2)print() 使用在任意的位置 都可以

def fun(x):
    return x%2  # 结束了函数，并将x%2结果提交给fun函数的调用处

if __name__ == '__main__':
    print(fun(10)) # 调用处 ，return 就将结果提交到这里，这个结果需要被处理（可以存储到变量中，也可以打印输出


