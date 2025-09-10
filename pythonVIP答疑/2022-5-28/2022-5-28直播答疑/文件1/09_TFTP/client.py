import os.path

from Socket import *


class CSocket(Socket):
    subclass_path = __file__
    handler_items = {1: 'w', 2: 'r'}

    def __init__(self):
        super().__init__()

    def request(self):
        exit_str = 'exit!!'

        self.while_state_items['input'] = True
        self.f_path = ''

        while self.while_state_items['input']:
            print('-' * 80)

            input_str = input('请输入: [文件路径]\n').strip()
            input_arr = input_str.split('-')

            print('输入', input_str)

            try:
                if input_str.lower() == exit_str:
                    raise Exception(0, '正在结束..')

                o_code, f_path = input_arr
                o_code = int(o_code)

                if not f_path:
                    raise Exception(1, '输入的文件路径为空')

                self.send_socket = self.recv_socket = self.root_socket
                self.s_code = self.server_id

                # 上传时 文件不存在不需要发送数据
                if o_code == 2:
                    f_path = self.d_path + f_path

                    if not os.path.exists(f_path):
                        raise Exception(1, '输入的文件不存在')

                    self.f_path = f_path

                self.send(o_code, f_path)

                if o_code == 1:
                    self.set_f_path(f_path)

                self.o_code = o_code
                self.while_state_items['input'] = False

            except (Exception, BaseException) as e:

                e_id, *e_args = e.args

                if e_id == 0:
                    self.while_state_items['main'] = False

                print('信息', e_id, *e_args, input_str)
                print()

    def main_init(self):
        self.request()  # 客户端需要发送数据

    def handler_init(self):
        pass


if __name__ == '__main__':
    CSocket().main()
