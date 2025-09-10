# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#
count=0
for x in range(50):   #为什么是50  ，50*50=2500 ， 40*40  =1600
    for y in range(50):
        for z in range(50):
            #判断
            if pow(x,2)+pow(y,2)+pow(z,2)==2009:
                print('x+y+z=',(x+y+z))
                count+=1

print(f'一共有{count}种可能')

# 结果放到集合中，集合有个特点叫自动去重

# 鸡兔同笼问题，百钱买百鸡问题
# 鸡+兔=35
# 2*鸡+4*兔=94
x=35   # x表示是总个数
y=94
for i  in range(1,x+1):  #i表示的是鸡的个数
    j=x-i   # j表示是兔的个数
    if 2*i+4*j==y:
        print(f'鸡的个数:{i},兔子的个数{j}')

# 百钱买百鸡
# 公鸡 5文，母鸡  3文，小鸡  1文3只

for i in range(1,101):   # i公鸡
    for j in range(1,101):  # j是母鸡
        for k in range(1,101):  #  k是小鸡
            if i*5+j*3+k/3==100 and i+k+j==100:
                print(f"公鸡{i}只，母鸡{j}只，小鸡{k}只")
