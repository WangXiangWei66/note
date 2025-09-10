import logging
import logging.handlers
from flask import request
import os


class RequestShoppingFormatter(logging.Formatter):
    """
    个性化的输出格式
    """
    def format(self, record):
        # 重写以下代码，用于下次调用record时，可直接完成对应的需求
        record.url = request.url    # 需要在日志中记录的请求地址
        record.remote_addr = request.remote_addr  # 需要在日志中记录客户端的地址
        return super().format(record)   # 将重写好的代码放回源代码中，重新调用更新过后的源代码，以便实现所需的要求




# 创建一个个性化的logger对象
def create_logger(app):
    """
    设置日志配置
    :param app: Flask中的app对象
    :return:
    """
    logging_file_dir = app.config['LOGGING_FILE_DIR']   # 日志文件所在目录
    logging_file_max_bytes = app.config['LOGGING_FILE_MAX_BYTES']  # 日志文件最大的大小
    logging_file_backup = app.config['LOGGING_FILE_BACKUP']  # 保留备份的日志文件个数
    logging_level = app.config['LOGGING_LEVEL']  # 默认的日志级别

    # 设置日志的输出格式(针对文件)
    request_formatter = RequestShoppingFormatter('[%(asctime)s] %(remote_addr)s 请求 %(url)s \t %(levelname)s 在 %(modules)s %(lineno)d : %(massage)s')


    # 检查如果目录不存在，则创建目录
    if os.path.isdir(logging_file_dir):
        pass
    else:
        os.mkdir(logging_file_dir)  # 目录不存在，则创建目录

    # 自定义一个目录和日志文件
    flask_file_handler = logging.handlers.RotatingFileHandler(filename=os.path.join(logging_file_dir, 'shopping.log'),
                                         maxBytes=logging_file_max_bytes,
                                         backupCount=logging_file_backup)

    # 给当前的handler设置格式
    flask_file_handler.setFormatter(request_formatter)

    # 得到一个logger 对象(将之前自定义的组成一个logger模型)
    flask_logger = logging.getLogger('Shopping')
    flask_logger.addHandler(flask_file_handler)
    flask_logger.setLevel(logging_level)

    # 整个项目需要两个hander：一个用于文件，一个用于控制台
    flask_console_hander = logging.StreamHandler()
    flask_console_hander.setFormatter(logging.Formatter('[%(asctime)s]  %(levelname)s %(levelname)s 在 %(modules)s %(lineno)d : %(massage)s'))


    # 当项目运行环境是debug，才用控制台输出, 在真正生产环境下，是一个纯净界面
    if app.debug:
        flask_logger.addHandler(flask_file_handler)
