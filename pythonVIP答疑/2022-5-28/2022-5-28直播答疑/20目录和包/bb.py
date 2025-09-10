# coding:utf-8
# author:杨淑娟
from directorydemo import a #由于driectorydemo是目录，所以报错 ModuleNotFoundError: No module named 'directory'
from packagedemo import aa # 正常执行，不报错，因为packagedemo是Python的包

# 目录，directory 不能使用from ...import
#  package  可以使用from ..import
