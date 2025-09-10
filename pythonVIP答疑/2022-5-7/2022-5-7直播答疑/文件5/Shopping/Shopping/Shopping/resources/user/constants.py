# 根据手机号限制短信验证码发送的频次
LIMIT_SMS_CODE_BY_MOBILE = '1/minute'


# 根据客户端IP限制短信发送的频次
LIMIT_SMS_CODE_BY_IP = '10/hour'

# 短信验证码存放到redis数据库中的时效
SMS_CODE_EXPIRES = 5 * 60