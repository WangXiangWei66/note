# coding:utf-8
# author:杨淑娟
import openpyxl
wk=openpyxl.load_workbook('test.xlsx')
sheet=wk.active  # 获取当前工作表
print(sheet['A1'].value, sheet['B1'].value)
print('没有数据'if sheet['A1'].value==None else '有数据') #与None是否相等