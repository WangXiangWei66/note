def odd(max):
    n = 1
    count = 0
    while True:
        yield n
        n += 2   # 3  ,5
        count = count + 1  #  3
        if count == max:
            #raise StopIteration
            #return
            break


odd_num = odd(3)
for num in odd_num:
    print(num)
