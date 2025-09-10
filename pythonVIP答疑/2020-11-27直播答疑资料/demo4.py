# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
#　ctrl+/   批量注释和批量取消注释
f=open('test2.txt','r',encoding='utf-8')
#print(f.read(7)) # 7个字符
#print(f.read(2))  #一个中文也表示一个字符

f.seek(6)   # 中国你好   想读取  你好
print(f.read())
f.close()    #一个utf-8的中文字符占三个字节  一个gbk的中文字符占2个字节

# seek(字节数)  中文 gbk， 跳过的就是2的倍数，utf-8跳过的就是3的倍数
# read(n) 读到的字符数


