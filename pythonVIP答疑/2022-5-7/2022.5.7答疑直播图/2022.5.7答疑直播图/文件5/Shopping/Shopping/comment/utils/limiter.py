from flask_limiter import Limiter   # limiter 限流器
from flask_limiter.util import get_remote_address   # 获取当前客户端IP地址

# 创建限流器
limiter = Limiter(key_func=get_remote_address)
