# result.png
import os.path
import pickle
import time
from socket import *

server_id = 'localhost', 69
b_size, r_size = 512, 1024


def get_time():
    return time.strftime('%X')


def print_plus(*args):
    # 输出优化 如果传入的是 b 返回长度
    if type(args[-1]) in [tuple, list]:
        args = list(args)
        args[-1] = list(args[-1])

        for k, item in enumerate(args[-1]):
            if type(args[-1][k]) == bytes:
                args[-1][k] = len(item)

        args = tuple(args)

    print(*args, get_time(), sep=' | ')


def o_socket():
    return socket(AF_INET, SOCK_DGRAM)


class Socket:
    server_id = server_id
    b_size, r_size = b_size, r_size

    subclass_items = dict(client='客户端', server='服务端')
    subclass_path = ''
    handler_items = {}

    def __init__(self):
        self.while_state_items = {'main': True}

        self.d_path = os.path.split(self.subclass_path)[1][:-3] + '/'
        self.f_path = ''

        if not os.path.exists(self.d_path):
            os.makedirs(self.d_path)

        self.root_socket = o_socket()
        self.send_socket = None
        self.recv_socket = None
        self.s_code = ()
        self.o_code = -1

        print_plus('socket 已开启', self.root_socket)

    def send(self, o_code, *args):
        o_code = int(o_code)
        s_data = pickle.dumps([o_code, *args])
        s_data_len = len(s_data)

        if not self.send_socket:
            return

        self.send_socket.sendto(s_data, self.s_code)

        if s_data_len > self.r_size:
            return
            # raise Exception(1, '消息', '错误', '发送数据大于%d' % self.r_size)

        print_plus('消息', '发送', self.s_code, o_code, args)

    def recv(self):
        if not self.recv_socket:
            return

        r_data, self.s_code = self.recv_socket.recvfrom(self.r_size)
        o_code, *r_args = pickle.loads(r_data)
        o_code = int(o_code)

        print_plus('消息', '接收', self.s_code, o_code, r_args)

        return o_code, *r_args

    def r(self):
        # self.f_path
        # 服务端需要  r_args[0]设置 并且需要判断文件是否存在
        # self.send(5, 1000, '文件不存在', r_args)

        if not self.f_path:
            return

        self.send_socket = self.recv_socket = data_socket = o_socket()

        self.while_state_items['r'] = True

        io = open(self.f_path, 'rb')
        b_code = 0

        e_id = -1
        e_items = {1001: '发送完成', 1002: 'ACK错误'}

        while self.while_state_items['r']:
            b_code += 1
            io_read = io.read(self.b_size)

            self.send(3, b_code, io_read)

            if len(io_read) < self.b_size:
                e_id = 1001

            o_code, *r_args = self.recv()  # 阻塞

            if o_code != 4 or r_args[0] < 1:
                e_id = 1002

            if e_id > 0:
                self.while_state_items['r'] = False

        if e_id in e_items:
            print_plus(e_items[e_id])
            print()

        io.close()
        data_socket.close()

    def set_f_path(self, f_path):
        s_path = os.path.splitext(f_path)
        f_path = self.d_path + s_path[0] + '_1_' + str(int(time.time())) + s_path[1]

        self.f_path = f_path

    def w(self):
        if not self.f_path:
            return

        self.while_state_items['w'] = True

        io = open(self.f_path, 'ab')
        state_id = -1
        state_items = {1001: '接收完成', 1002: '读取端文件不存在'}

        while self.while_state_items['w']:
            o_code, *r_args = self.recv()

            # 仅客户端有用
            if o_code == 5:
                state_id = 1002
                self.while_state_items['w'] = False

            if o_code == 3:
                b_code, io_read = r_args

                io.write(io_read)

                if len(io_read) < 512:
                    state_id = 1001
                    self.o_code += 1
                    self.while_state_items['w'] = False

                self.send(4, b_code)

        if state_id in state_items and state_id != 1002:
            print_plus(state_items[state_id])
            print()

        io.close()

        # 客户端所需
        if state_id == 1002:
            os.unlink(self.f_path)

    def main_init(self):
        pass

    def handler_init(self):
        pass

    def main(self):
        while self.while_state_items['main']:
            self.main_init()

            if self.o_code in [1, 2]:
                self.handler_init()
                eval('self.' + self.handler_items[self.o_code] + '()')


if __name__ == '__main__':
    pass

# result.png
# 单客户端 不能多个客户端同时下载 如果一个客户端在下载,另一个就会等下载完成再下载(收到数据包)
# 独立写两部分 下载上传都可以 如何优化问题了
