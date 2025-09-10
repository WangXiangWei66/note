import re


def mobile(mobile_str):
    """
    检验手机号格式
    :param mobile_str: str 被检验字符串
    :return: mobile_str
    """
    if re.match(r'^1[3-9]\d{9}$', mobile_str):
        return mobile_str
    else:
        raise ValueError('{} is not a valid mobile'.format(mobile_str))


def regex(pattern):
    """
    正则校验
    :param pattern: str 正则表达式
    :return: 返回一个函数
    """
    def validate(value_str):
        """
        具体校验一个字符串,根据自定义的正则表达式
        :param value_str: 验证的值
        :return:
        """
        if re.match(pattern, value_str):
            return value_str
        else:
            raise ValueError('{} is invalid params.'.format(value_str))

    return validate


def email(email_str):
    """
        检验邮箱地址格式
        :param email_str: str 被检验字符串
        :return: email_str
        """
    if re.match(r'^([A-Za-z0-9_\-\.\u4e00-\u9fa5])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,8})$', email_str):
        return email_str
    else:
        raise ValueError('{} is not a valid email'.format(email_str))

