#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

def fun():
    s=input('请输入一个整数：')
    if not s.isdigit():
        raise Exception('非整数') # 手动抛出异常

# 将在函数 的调用处理异常
try:
    fun()  # 可能产生异常
except Exception as e:
    print(e)


