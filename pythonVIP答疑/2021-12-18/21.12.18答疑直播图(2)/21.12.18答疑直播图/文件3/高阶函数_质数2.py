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

def prime():
    p = get_odd()
    while True:
        n = next(p)
        p = filter(lambda x: x % n > 0, p)
        yield n

prime1 = prime()
for i in range(20):
    print(next(prime1))
