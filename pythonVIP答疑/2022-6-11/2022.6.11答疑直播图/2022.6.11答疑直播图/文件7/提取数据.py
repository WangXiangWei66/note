import os
import shutil
path=input('要提取的文件夹地址:')#xzx,C:\Users\Administrator\Desktop\psaic4d
path_new=input('要保存文件夹地址:')#x
for root,dirs,files in os.walk(path):#root,dirs,files
    for i in range(len(files)):
        # print(files[i])
        if (files[i][-3:]=='jpg') or (files[i][-3:]=='png'):
            file_path=root+'/'+files[i]
            shutil.copy(file_path,path_new)
