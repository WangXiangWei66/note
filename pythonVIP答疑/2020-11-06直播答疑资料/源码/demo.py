# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
a=str(5)
#8:03 公布答案
lst=[eval(a*i) for i in range(1,3)]  # '5'*1  '5'*2  结果为55
print(lst)
print(sum(lst)) # 结果是什么？60


print(sum(eval('5*i') for i in range(1,3)))  # 5*1 , 5*2  5+10

eval('print(520)')  #eval函数的作用，去掉左右的单引号，print(520)

