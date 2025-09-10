import os.path

from Socket import *


class SSocket(Socket):
    subclass_path = __file__
    handler_items = {1: 'r', 2: 'w'}

    def __init__(self):
        super().__init__()
        self.root_socket.bind(('', self.server_id[1]))
        self.recv_socket = self.root_socket

        self.recv_args = ()

    def main_init(self):
        self.send_socket = self.recv_socket = self.root_socket

        self.o_code, *self.recv_args = self.recv()

    def handler_init(self):
        if self.o_code == 1:
            f_path = self.d_path + self.recv_args[0]

            if not os.path.exists(f_path):
                self.send(5, 1000, '下载的文件不存在', self.recv_args)
                return

            self.f_path = f_path

        elif self.o_code == 2:
            self.set_f_path(self.recv_args[0])


if __name__ == '__main__':
    SSocket().main()
