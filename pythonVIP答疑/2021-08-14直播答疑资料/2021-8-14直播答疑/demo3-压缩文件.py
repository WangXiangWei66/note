# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import zipfile
import os
file_list=['text.txt','fda','压缩包.zip'] # 准备解缩的内容
with zipfile.ZipFile('压缩包33.zip','w') as zipobj:
    # print(zipobj.namelist())
    for file in file_list:
       if os.path.isdir(file): # 判断file是不是文件夹
           lst2=os.listdir(file) # 获取文件夹下的所有文件列表
           for item in lst2:  #如果lst2中还有文件夹，还需要继续判断，解决方案—使用递归
               zipobj.write(file+'\\'+item ) # 用到了路径的拼接

       zipobj.write(file)