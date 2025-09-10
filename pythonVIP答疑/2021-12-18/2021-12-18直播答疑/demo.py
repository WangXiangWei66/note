# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟


#．生成柱状图时，可以选择单词数量（如生成前10个高频词的柱状图)

#Python中有个第三方模块叫jieba，可以实现中文分词 pip install jieba
import jieba
import pandas    # 安装方式  pip install pandas
import matplotlib.pyplot as plt  # 安装方式 pip install matplotlib

with open('告别日落.txt','r') as file:
    s=file.read()  #读取全部内容

lst=jieba.lcut(s) #
#print(len(lst)) # 清洗之前词的长度
#print(lst)
# 清洗
# for item in lst:
#     if len(item)<2 or item=='\u3000' or item=='\n':
#         lst.remove(item)
# print(len(lst)) # 清洗之后词的长度

# 统计词语的个数

s=set(lst) # 将lst转成集合 ，去重
# 统计个数
d={}  # key是词，value是词出现的次数
for item in s:
    d[item]=0   #所有键所对象的次数都是0

#遍历列表
for item in lst:
    if item in d:
        d[item]=d.get(item)+1 #给键赋值

#print(d)

# 转成列表, 每个小列表中有两个元素【key,value】
new_lst=[]

for item in d:
    if len(item)>=2: # 组成词语的中文字数，大于等于2个
        new_lst.append([item,d.get(item)])


# 对列表进行排序  x是new_lst中的元素，
new_lst.sort(key=lambda x:x[1],reverse=True) # 降序，排序的规则，使用小列表中的个数排序

#print(new_lst)
new_lst=new_lst[:11] # 切片获取前10项
#print(new_lst)
# 绘制图表

# 设置画布大小
plt.figure(figsize=(10,6))

# 解决中文乱码
plt.rcParams['font.sans-serif']=['SimHei']

# 设置x轴和y轴数据
x_lst=[]  # 词语是x轴
y_lst=[]  # 词语出现的次数是y轴

for item in new_lst:
    x_lst.append(item[0]) # 添加x轴的数据
    y_lst.append(item[1]) # 添加y轴的数据


x=pandas.Series(x_lst) # 将列表转成Series类型
height=pandas.Series(y_lst)

# 柱子上现出次数
for a,b in zip(x,height):
    plt.text(a,b,format(b,','),ha='center',va='center',fontsize=12,color='b',alpha=0.9)
# 绘图
plt.bar(x,height,width=0.5,alpha=0.5)

plt.show() # 显示





