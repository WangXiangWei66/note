# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

from socket import *
import struct

server = socket(AF_INET,SOCK_STREAM)
server.bind(('',8088))
server.listen(5)

conn,addr = server.accept()

f  = open(r'D:\服务器.mp4','wb')

header_data = conn.recv(4)
size = struct.unpack("!i",header_data)[0] #unpack返回的都是一个元组,元组的第一个值就是长度

recv_size = 0 #已经接受到多长的数据
while recv_size < size:
    data = conn.recv(1024)
    recv_size += len(data) #结束的字节长度要累加
    f.write(data)

print("服务器端接受完成")
f.close()
conn.close()
server.close()


