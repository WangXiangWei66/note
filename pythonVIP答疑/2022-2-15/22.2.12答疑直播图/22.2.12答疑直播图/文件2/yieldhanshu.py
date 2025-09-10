def odd(max):
    n = 1
    count = 0
    while True:
        yield n
        n += 2
        count = count + 1
        if count == max:
            raise StopIteration


odd_num = odd(3)
for num in odd_num:
    print(num)
