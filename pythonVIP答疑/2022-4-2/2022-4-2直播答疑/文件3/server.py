# coding:utf-8
# author:杨淑娟
from socket import *
import struct
#服务器端的socket
s = socket(AF_INET,SOCK_DGRAM)

#绑定IP和端口号
s.bind(('',69))#不能s.bind('',69) 因为bind函数里面只能传一个参数，所以要先封装成一个元组，再作为参数传进函数


def download(filename,client_ip,client_port):

    #创建一个新的Socket，负责发送文件内容的数据包到客户端
    new_socket = socket(AF_INET,SOCK_DGRAM)

    #文件内容数据包的计数器,起始就是快的编号
    num = 1

    #定义服务客户端退出的标签
    flag = True
    f=''
    try:
        f =open(filename,'rb')
    except:#except后面没有接异常类型，则可以接收所有异常   #这里是想如果文件不存在就执行
        error_package = struct.pack('!HH5sb',5,5,'error'.encode('utf-8'),0) #H 表示python的Integer转成C的没有符号的short，5s表示把Python中包含5个字符的字符串转成C的字符数组
        new_socket.sendto(error_package,(client_ip,client_port)) #把错误数据包发给客户端
        # exit() #当前线程结束，当前socket结束，当前客户端退出服务器
        flag =False

    #如果文件存在，那么需要把文件的内容切成一个个的数据包发送给客户端，一个数据包包含数据内容为512字节
    while flag:
        #从文件内容中读取512字节
        read_data = f.read(512)
        #创建一个数据报
        data_package = struct.pack('!HH',3,num) + read_data
        #发送数据包
        new_socket.sendto(data_package,(client_ip,client_port))
        if len(read_data) < 512: #文件内容的数据刚好读完
            print("客户端:%s,文件下载完成"%client_ip)
            break
        #服务器接收ACK的确认数据
        recv_ack = new_socket.recvfrom(1024) #里面有数据包的内容，还有客户端的IP和端口
        operator_code,ack_num = struct.unpack('!HH',recv_ack[0])
        print("客户端：%s,的确认信息是"%client_ip,ack_num)
        num +=1
        #保护性代码
        if int(operator_code) !=4 or int(ack_num) <1: #不正常的ack确认信息
           break
    if f:
        f.close()
    new_socket.close() #客户端真正退出了


def server():

    while True:

        #服务器等着客户端发送过来数据，然后等着接收
        recv_data,(client_ip,client_port)= s.recvfrom(1024)
        print(recv_data,client_ip,client_port)

        #判断数据包是否是：客户端请求的数据包    问题1
        print( struct.unpack('!b5sb',recv_data[-7:]))
        print(recv_data[-7:].decode('utf-8'))

                # b5sb  0，octet,0                     # 为什么要加上b
        if struct.unpack('!b5sb',recv_data[-7:]) == (0,b'octet',0):#此时octet还是字节数据，所以要加b''。此时还没有解码。  但是整数就不用加b''，比如0
            #得到操作码的值
            operator_code = struct.unpack('!H',recv_data[:2]) #操作码占两个字节，它的内容是一个1或2。所以用一个H即C语言中的short类型（short类型占两个字节）。然后把0看成char类型（char类型占一个字节，用b）
            #得到文件名字                         问题2

            print(type(recv_data[2:-7])) # bytes类型

            file_name = recv_data[2:-7].decode('utf-8') #这里不用解包就能得到文件名原因：b'text.jpg'这种通过decode就可以直接将字节转成字符串（而且已经c语言-->python了）
            print(operator_code,file_name)#struct.unpack()的结果是一个元组（1,），所以下面要[0]取出操作码的数据
            if operator_code[0] ==1: #如果等于1就是下载的请求数据包
                print("客户端想下载文件：%s"%file_name)
                download(file_name,client_ip,client_port)


if __name__ == '__main__':
    server()
