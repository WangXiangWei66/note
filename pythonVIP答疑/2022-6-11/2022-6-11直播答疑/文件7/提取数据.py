import os
import shutil

#更确切的说是文件的复制（图片文件的复制）
path=input('要提取的文件夹地址:')#xzx,C:\Users\Administrator\Desktop\psaic4d
path_new=input('要保存文件夹地址:')#x
for root,dirs,files in os.walk(path):#root,dirs,files
    for i in range(len(files)):
        # print(files[i])
        if (files[i][-3:]=='jpg') or (files[i][-3:]=='png'):  # 在这判断了文件的类型， jpg或者png的图片才执行复制
            file_path=root+'/'+files[i]
            shutil.copy(file_path,path_new)
