# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#pip install ipython
#内置函数
with open('aa.txt','w') as file:
    file.write('helloworldddddddd')


# 第三方库pandas保存文件
import  pandas as pd
df=pd.DataFrame([[1,2,3],[4,5,6]],columns=['A','B','C'])
df.to_excel('a.xlsx',index=False)
df.to_csv('a.csv',index=False)

#内置模块csv
import csv  # csv文件又叫逗号分隔值
with open('b.csv','w') as file:
    write=csv.writer(file)
    write.writerow(['张三',20,98.5])

# numpy保存
import numpy as np
array=np.array([[11,2,3],[3,56,676]]) # 创建一个数组
np.savetxt('b.txt',array) # 把数组中的数据保存成txt文件


