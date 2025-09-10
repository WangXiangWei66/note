# 教育机构：马士兵教育
# 讲    师：杨淑娟
def guess(guessnum,heartnum):
    if guessnum<heartnum:   #小于的情况
        return -1
    elif guessnum>heartnum: #大于的情况
        return 1
    else:
        return 0  #等于的情况

import random
if __name__ == '__main__':
    rand=random.randint(1,100) #心里的数
    for i in range(1,11):
        num=eval(input('1-100之间的数，你猜猜'))
        res=guess(num, rand) #调用函数
        if res>0:
            print('大了')
        elif res<0:
            print('小了')
        else:
            print('猜对了')
            break

        #次数判断
    print('您一共猜了{}次'.format(i))
    if i<3:
        print('真聪明')
    elif 3<=i<7:
        print('还凑合')
    else:
        print('天啊....')







