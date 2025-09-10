# coding:utf-8
# author:杨淑娟
#定义了一个函数，函数的名称叫 eat
def eat():
    print('我正在吃饭')

def test1(func): #定义的第2个函数，函数的名称叫test1,参数--》形式参数 ，func
    def test2():  #  函数内部定义的函数  （函数的嵌套)
        print('帮你把饭做好')
        func() # 调用函数    ------->   func形参的名称，形参是一个函数，调用函数
        print('洗碗')
    return test2     # test1函数的返回值 ，该 返回值是一个函数


# 想调用test1函数
# eat=test1(func=eat)   # 关键字传参  ,返回值是一个函数，
# eat()  # 调用test1这个函数的返回值

@test1   # 这就是一个语规则， 只要是使用@ xxx
def eat():
    print('我正在吃饭')

# 调用test1时，直接写
eat()   # 这个eat就相当于 16,17两行代码的功能