# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
# ctrl键
# 在Python中 以.py结束的文件就称为一个模块
import  random
print(random.random()) # 产生一个[0,1)之间的随机数
print(random.randint(1,10)) # 包含不包含10呢？ [1,10] 双闭区间，包含10
print('---------------------------')
for i in range(10):
    print(random.randrange(1,10),end='\t') # 包含不包含10？ [1,10)  randrange(start,stop,step)

print('----------------------------------')
lst=[10,4,53,455,67,784,34]  # 列表
print(random.choice(lst))  # 每次运行的效果都不同,从列表中随机获取一个元素
print('lst:',lst)
random.shuffle(lst)  # 打乱排序
print('lst',lst)







