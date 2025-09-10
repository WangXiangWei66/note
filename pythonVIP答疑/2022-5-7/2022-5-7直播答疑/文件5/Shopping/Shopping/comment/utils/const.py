# -*- coding: utf-8 -*-
import os
# ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
# AccessKeyId用于标识用户
ACCESS_KEY_ID = "LTAI5tH21vuCvZwvjbrZJ1Ea"
ACCESS_KEY_SECRET = "8LJXHdiXJ6OY5nlmH7JbuD8LNt1lZf"

SECRET_KEY = os.urandom(16)  # 生成一个随机数作为秘钥
JWT_EXPIRY_SECOND = 60*60 # TOKEN的有效时间


