# Grewizard 编辑
# 开发时间: 2022/6/29 10:34
import os
import xlwt as xl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import openpyxl

#创建表格
nipdata=xl.Workbook()
sheet1=nipdata.add_sheet('nip数据',cell_overwrite_ok=True)  #给表格1命名
sheet1.write(0,0,'编号')
sheet1.write(0,1,'Time')
sheet1.write(0,2,'RollerID')
sheet1.write(0,3,'Clothtype')
sheet1.write(0,4,'User')
sheet1.write(0,5,'Depth')
sheet1.write(0,6,'Nip')

#抓取指定路径数据，将数据写入excel并保存
n=0
file_dir="C:/Users/110130/Desktop/Nip"   #文件处理的路径
for i,j,k in os.walk(file_dir): #返回值为路径、文件夹名、文件名
    while n< len(k):
        sheet1.write(n+1,0,n+1)
        Time=str(k[n])[0:8]
        sheet1.write(n+1,1,Time)
        RollerID=str(k[n])[9:13]
        sheet1.write(n + 1, 2, RollerID)
        Clothtype = str(k[n])[14:20]
        sheet1.write(n + 1, 3, Clothtype)
        User=str(k[n])[21:29]
        sheet1.write(n + 1, 4, User)
        Depth=float(str(k[n])[35:39])
        sheet1.write(n + 1, 5, Depth)
        Nip=float(str(k[n])[30:34])
        sheet1.write(n + 1, 6, Nip)
        n=n+1
nipdata.save('C:/Users/110130/Desktop/Nip.xls')

#线性回归分析
df=pd.read_excel('C:/Users/110130/Desktop/Nip.xls')
plt.figure(figsize=(8,6))
plt.scatter(df['Depth'],df['Nip'],label='Depth-Nip')
plt.legend(loc='best')

result=smf.ols('Nip~Depth',data=df,).fit()
print(result.params)
print(result.summary())

y_fitted=result.fittedvalues
plt.plot(df['Depth'],y_fitted,'r-',label='ols')
plt.plot(df['Depth'],df['Nip'],'o',label='Depth-Nip')
plt.show()

# 线性拟合结果保存至excel
