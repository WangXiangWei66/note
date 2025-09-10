# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import  openpyxl
wk=openpyxl.load_workbook('Book1.xlsx') #打开工作簿
#获取活动工作表
sheet=wk.active
#遍历工作表
for row in sheet.rows: #行
    for cell in row: # 从行中遍历单元格
        print(cell.value,end=' ')
    print()

