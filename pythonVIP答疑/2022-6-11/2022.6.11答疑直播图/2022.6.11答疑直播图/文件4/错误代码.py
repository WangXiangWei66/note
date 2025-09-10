import socket
import time
import sys
import threading


class MyHttpWebServer(object):

        def __init__(self, port):
            #  ����HTTP������׽���
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # ���ö˿ںŸ���, �����˳�֮����Ҫ�ȴ������ӣ�ֱ���ͷŶ˿�
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            server_socket.bind(('', port))
            # ���÷���������
            server_socket.listen(128)
            # ����Ϊ��Ա����--��ʼ���׽���
            self.server_socket = server_socket

        @staticmethod
        def handle_browser_request(new_socket):
            # ���տͻ��˷���������
            recv_data = new_socket.recv(4096)
            # ���û���յ����ݣ���ô������Ч���ر��׽��֣�ֱ���˳�
            if len(recv_data) == 0:
                new_socket.close()
                return
            # ���յ����ֽ����ݣ���Ҫ���н���
            request_data = recv_data.decode('utf-8')
            print("�������������ݣ�", request_data)
            request_array = request_data.split('', maxsplit=2)
            # �õ�������·��
            request_path = request_array[1]
            print("����·��", request_path)
            if request_path == '/':  # webϰ�ߣ��������·��Ϊ��Ŀ¼���Զ�����Ϊ/index.html
                request_path = '/index.html'

            # ��������·�����ж��Ƕ�̬��Դ���Ǿ�̬��Դ
            if request_path.endswith('.html'):
                '''��̬��Դ������'''
            else:
                '''��̬��Դ������'''
                # ��������·����ȡ/staticĿ¼�о�̬�ļ����ݣ���Ӧ���ͻ���
                try:
                    # ��ȡstaticĿ¼�ж�Ӧ���ļ�����,rbģʽ����һ�ּ���ģʽ�����Դ�ͼƬ��Ҳ���Դ�js�ļ�
                    with open('static' + request_path, 'rb') as f:
                        file_content = f.read()
                except Exception as e:  # ��������ȡ���ļ����ܲ�����
                    with open('static/404.html', 'rb') as f:
                        response_body = f.read()  # ��Ӧ����������
                    # ��Ӧͷ
                    response_hander = 'HTTP/1.1 404 Not Found\r\n' + 'Content-Length:' + str(len(response_body)) + '\r\n' + 'Content-Type: text/html; ' 'charset=utf-8\r\n' + 'Date:' + time.strftime('%Y-%m-%d %H%M%S', time.localtime()) + 'Server: myserver \r\n'
                    # �����Ӧ���ݷ��͸����������
                    response = (response_hander + '\r\n').encode('utf-8') + response_body
                    new_socket.send(response)

        # ���������������տͻ��˵�����
        def start(self):
            # ѭ�����Ҷ��̵߳Ľ��տͻ��˵�����
            while True:
                new_socket, ip_port = self.server_socket.accept()
                print("�ͻ��˵�ip�Ͷ˿�", ip_port)
                # һ���ͻ��˵����󽻸�һ���̴߳���
                sub_thread = threading.Thread(target=MyHttpWebServer.handle_browser_request, args=(new_socket,))
                sub_thread.setDaemon(True)  # ���õ�ǰ�߳�Ϊ�ػ��߳�
                sub_thread.start()  # ���߳�����


def mian():
    web_server = MyHttpWebServer(8080)
    web_server.start()


if __name__ == '__main__':
    # ip: 192.168.0.106
    mian()
