# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

# 买衣服的
i=1 # 表示第几家店
total=0 # 总共买衣服的件数
while True:
    print('欢迎光临第'+str(i)+'家小店') # 因为str+int报错
    count=0

    while True:  #开始挑选衣服
        answer=input('这件衣服买吗?')
        if answer=='y':
            count+=1
        else:
            break # 退出这个店


    print(f'在第{i}家小店，买了{count}件衣服')
    total+=count
    i+=1
    an=input('还继续逛吗？')
    if an=='n':
        break

print(f'一共逛了{i}家店，买了{total}件衣服')