# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import os
def file_name(file_dir):
   for root,dirs,files in os.walk(file_dir):
       for i in dirs:
           if '（添加售后VX：kcr088)' in i:
               #改名可以使用替换
                a=i.replace('（添加售后VX：kcr088)','')
                #拼接路径
                i=os.path.join(root+'\\'+i)
                a=os.path.join(root+"\\"+a)
               # 重命名  将 i 这个变量的名称，改成a这个变量的名字
                os.rename(i,a)


for root ,dirs,files in os.walk('./data'):
    for item in root:
        file_name(item)