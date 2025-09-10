# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
count=0
while True:    #条件判断，条件判断的结果为True
    print("helloworld")
    count+=1 #每输出一次，就累加一次
    if count==5:  # 判断的退出条件
        break

print('循环结束之后的内容')
i=0
while i<5:   #条件判断 i=0时，True， i=1,True,i=2,True,i=3，True，i=4,True,i=5,False
    print("helloworld")
    i+=1
print('循环之后的内容')