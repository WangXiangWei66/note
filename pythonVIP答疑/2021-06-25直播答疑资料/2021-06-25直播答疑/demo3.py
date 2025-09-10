# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import time
isBirthday=False
def get_birth():
    # 获取全局变量
    global isBirthday
    # 获取系统时间
    date=time.strftime("%Y-%m-%d", time.localtime(time.time()))
    if date=='2021-06-25':
        print("今天是您的生日，全场8折优惠哦~~")
        isBirthday=True  # 为什么是灰的色的 ，因为13行定义是局部变量，这个变量只定义了，以没有被使用过，所以是灰色的
        print(isBirthday)
get_birth()
print('全局',isBirthday)

# 不可变对象，修改值就等于修改id