# coding:utf-8
# author:杨淑娟
# -*- coding: utf-8 -*-
from socket import *
import struct #专门负责Python数据结构和c语言数据结构转换，变成c语言能够识别的字节流
file_name = input("请输入文件名字:")


#客户端的Socket
s = socket(AF_INET,SOCK_DGRAM)

#定义目标服务器的地址和端口号
host_port = ('localhost',69)
# "!H%dsb5sb" 代表格式：！开头，请求的数据包
#     struct.pack(格式，操作码（1是下载），文件名（bytes）0,模式[这个模式是确定的，octet ,C里面的字节],0)
 # 把Python里面的数据变成C里的数据  H--》无符号整数  %d  s是将Pyhton的字符串转成c的char[] %d 指的是len(file_name)
 # b-->signedchar (integer)把整型变字符  octet  5个s ,  b--》0
 # 打包数据      struct.pack(格式,操作码, 文件名 0, 模式,0)
 # 'octet'.encode('utf-8') 把Python的字符串类型转成bytes
data_package = struct.pack('!H%dsb5sb'%len(file_name),1,file_name.encode('utf-8'),0,'octet'.encode('utf-8'),0)  #pack是指将数据变成一个包，octet是固定不变的。这个octet是python中的字符串，再编码成字节数据，


#把数据包发到目标服务器
s.sendto(data_package,host_port)

#客户端首先创建一个空白文件
f = open('client_'+file_name,'ab')

while True:

    #客户端接收服务器发过来的数据，数据只有两种：1、下载文件内容数据报，2、error信息报
    recv_data, (server_ip, server_port) = s.recvfrom(1024)

    operator_code, num = struct.unpack('!HH',recv_data[:4]) #把前4个字节的数据解包出来

    if int(operator_code) ==5: #判断数据包是否是error信息报
        print("服务器返回：你要下载的文件不存在!")
        break

    #如果是文件内容的数据，需要保存文件内容
    f.write(recv_data[4:])

    if len(recv_data) < 516: #意味着服务器传输过来的文件已经接收完成了
        print("客户端下载成功")
        break

    #客户端收到数据包之后，还需要发送一个确认ACK给服务器
    ack_package = struct.pack('!HH',4,num)
    s.sendto(ack_package,(server_ip, server_port))

#释放资源
f.close()
s.close()
