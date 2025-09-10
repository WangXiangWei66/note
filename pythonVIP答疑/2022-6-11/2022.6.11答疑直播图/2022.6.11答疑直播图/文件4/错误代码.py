import socket
import time
import sys
import threading


class MyHttpWebServer(object):

        def __init__(self, port):
            #  创建HTTP服务的套接字
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 设置端口号复用, 程序退出之后不需要等待几分钟，直接释放端口
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            server_socket.bind(('', port))
            # 设置服务器监听
            server_socket.listen(128)
            # 设置为成员属性--初始化套接字
            self.server_socket = server_socket

        @staticmethod
        def handle_browser_request(new_socket):
            # 接收客户端发来的数据
            recv_data = new_socket.recv(4096)
            # 如果没有收到数据，那么请求无效，关闭套接字，直接退出
            if len(recv_data) == 0:
                new_socket.close()
                return
            # 接收的是字节数据，需要进行解码
            request_data = recv_data.decode('utf-8')
            print("浏览器请求的数据：", request_data)
            request_array = request_data.split('', maxsplit=2)
            # 得到了请求路径
            request_path = request_array[1]
            print("请求路径", request_path)
            if request_path == '/':  # web习惯，如果请求路径为根目录，自动设置为/index.html
                request_path = '/index.html'

            # 更据请求路径来判断是动态资源还是静态资源
            if request_path.endswith('.html'):
                '''动态资源的请求'''
            else:
                '''静态资源的请求'''
                # 根据请求路径读取/static目录中静态文件数据，响应给客户端
                try:
                    # 读取static目录中对应的文件数据,rb模式：是一种兼容模式，可以打开图片，也可以打开js文件
                    with open('static' + request_path, 'rb') as f:
                        file_content = f.read()
                except Exception as e:  # 浏览器想读取的文件可能不存在
                    with open('static/404.html', 'rb') as f:
                        response_body = f.read()  # 响应的主题内容
                    # 响应头
                    response_hander = 'HTTP/1.1 404 Not Found\r\n' + 'Content-Length:' + str(len(response_body)) + '\r\n' + 'Content-Type: text/html; ' 'charset=utf-8\r\n' + 'Date:' + time.strftime('%Y-%m-%d %H%M%S', time.localtime()) + 'Server: myserver \r\n'
                    # 组成响应内容发送给（浏览器）
                    response = (response_hander + '\r\n').encode('utf-8') + response_body
                    new_socket.send(response)

        # 启动服务器并接收客户端的请求
        def start(self):
            # 循环并且多线程的接收客户端的请求
            while True:
                new_socket, ip_port = self.server_socket.accept()
                print("客户端的ip和端口", ip_port)
                # 一个客户端的请求交给一个线程处理
                sub_thread = threading.Thread(target=MyHttpWebServer.handle_browser_request, args=(new_socket,))
                sub_thread.setDaemon(True)  # 设置当前线程为守护线程
                sub_thread.start()  # 子线程启动


def mian():
    web_server = MyHttpWebServer(8080)
    web_server.start()


if __name__ == '__main__':
    # ip: 192.168.0.106
    mian()
