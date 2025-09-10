#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# a和a+的区别
# a -->append 追加写模式
# +读写模式 ，但是+ 不能独立使用

with open('a.txt','a') as file:
    file.write('hello')
    file.write('world')
    # 把指针放到文件的最前边
    file.seek(0)
   # print(file.read()) #io.UnsupportedOperation: not readable

with open('b.txt','a+') as file:
    file.write('hello')
    file.write('world')
    # 把指针放到文件的最前边
    file.seek(0) #一定要加这句代码，否则指针在文件最后，是读不到数据的
    print(file.read())
