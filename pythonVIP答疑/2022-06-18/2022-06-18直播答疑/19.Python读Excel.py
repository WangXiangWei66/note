# coding:utf-8
# author:杨淑娟
import openpyxl  # 使用的是第3方模块openpyxl
wk=openpyxl.load_workbook('student.xlsx')  #
sheet=wk.active

d={}
total=[]
new_total=[]
for row in sheet.rows:
   lst=[]
   for cell in row:
       lst.append(cell.value)
   total.append(lst)
#print(total[1:])
for item in total[1:]:
    new_total.append(tuple(item))

#print(new_total)

d=dict(new_total) # 将列表转字典
print(d)
