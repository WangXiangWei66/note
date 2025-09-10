# coding:utf-8
# 时间：2022/4/30 18:25
# 描述：打印前100的素数

# 所有奇数
def all_odd_number():
    a = 1
    while True:
        a += 2
        yield a


# 所有素数
def prime_number():
    yield 2
    odd = all_odd_number()
    while True:
        o = next(odd)
        odd = filter(lambda x: x % o > 0, odd)
        yield o


if __name__ == '__main__':
    for index, item in enumerate(prime_number()):
        if item < 100:
            print(item, end=' ')
            if index % 10 == 0 and index != 0:
                print()

        else:
            break
