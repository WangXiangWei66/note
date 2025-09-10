# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

# 请输入您的利润
# 请输入您的利润
profit=int(input('Show me the money'))
bonus=0  # 奖金
# 奖金的起点
thresholds=[100000,100000,200000,200000,400000]
# 奖金比率
rates=[0.1,0.075,0.05,0.03,0.015,0.01]

# 循环遍历起点  #０，１，２，３，４的整数
for i in range(len(thresholds)): # 循环执行5次
    if profit<=thresholds[i]:
        bonus+=profit*rates[i] # 计算奖金的比例
        profit=0  # 利润清0
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)

