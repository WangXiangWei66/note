# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt # 第三方
df=pd.read_excel('学生.xlsx')
print(df)
# 提取数学及格的学生信息
print('----------------------')
new_df=df[df['数学']>=60]
print(new_df)

# 多柱形图
x=np.array([1,2,3,4])
y1=df['语文']
y2=df['数学']
y3=df['英语']
plt.rcParams['font.sans-serif']=['SimHei']

width=0.25  #柱形图的柱子宽度
plt.bar(x,y1,color='r',width=width)
plt.bar(x+width,y2,color='g',width=width)
plt.bar(x+2*width,y3,color='b',width=width)


# 各科加提示
for a,b in zip(x,y1):
    plt.text(a,b,'语文'+str(b),ha='center',va='bottom',fontsize=9)

for a,b in zip(x,y2):
    plt.text(a+width,b,'数学'+str(b),ha='center',va='bottom',fontsize=9)

for a,b in zip(x,y3):
    plt.text(a+2*width,b,'英语'+str(b),ha='center',va='bottom',fontsize=9)
plt.xticks(x, df['姓名'])
plt.title('学生成绩')
plt.show()
