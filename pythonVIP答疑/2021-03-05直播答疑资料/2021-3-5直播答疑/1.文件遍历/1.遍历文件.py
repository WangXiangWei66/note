# 教育机构：马士兵教育
# 讲    师：杨淑娟

import os
import  shutil  # 该模块中的copy方法，可用于文件的拷贝
path='D:/img'
for dirpath,dirnames,fs in os.walk('./images'):

    for item in fs:
        shutil.copy(dirpath+'/'+item, path+'/'+item)
