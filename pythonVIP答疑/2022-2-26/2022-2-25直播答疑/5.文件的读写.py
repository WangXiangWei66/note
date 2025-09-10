# coding:utf-8
# author:杨淑娟

# w是覆盖写， a是追加写
# 文件的写操作
  #a.txt文件的路径+文件名称  w 表示write， encoding 文件中汉字的编码格式，一个中文占三个字节
with open('a.txt','w',encoding='utf-8') as file :
    file.write('北京冬奥') # 4个中文，所以占磁盘12个字节, 如果不写编码格式，  占8个字节，默认编码格式为gbk
    file.write('\n')
    file.write('喜欢普京小老头')


# 文件的读操作  r表示read ,
with open('a.txt','r',encoding='utf-8') as file :
     # 使用read读全部
    #print(file.read())  # 结查是字符串
     # 使用readline读，一次读一行
     #print(file.readline())  # 结果是字符串
    # 使用readlines()读，结果是列表
    print(file.readlines())
