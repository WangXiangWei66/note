# 
# 作者：马千里
# 时间：2021/12/16 0016 9:19
# 

# 定义奇数生成器
def get_odd():
    n = 1
    while True:
        n += 2
        yield n

# 定义判断是否能整除高阶函数
def div(n):
    return lambda x: x % n > 0

def prime():
    p = get_odd()
    while True:
        n = next(p)
        p = filter(div(n),p)
        yield n

p = prime()
for i in range(20):
    print(next(p))
