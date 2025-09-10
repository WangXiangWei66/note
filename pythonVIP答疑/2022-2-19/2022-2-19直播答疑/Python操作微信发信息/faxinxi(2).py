import pyautogui    # 第三方模块，需要安装才能使用
import pyperclip   # 第三方模块，需要安装才能使用
import time


def get_msg():
    """想发的消息，每条消息空格分开"""
    contents = "做好防疫安全非必要不出门，减少出行。出门记得戴口罩，勤洗手。 注意饮食安全，杜绝孩子暴饮暴食，不吃生冷辛辣食物，不乱吃零食。 假期外出注意交通安全，不独自过马路或在路上乱跑。不玩水、电、火、鞭炮，外出活动一定要有家长陪同。 注意合理安排好孩子的作息时间，早睡、早起，不可长时间看电视、玩手机，尽量保持作息规律，以免孩子放假返校后出现不适应的现象。 家长尽量抽空陪同孩子做做游戏、讲讲故事等，让孩子感受假期里家庭的温馨。 "
    return contents.split(" ")


def send(msg):
    # 复制需要发送的内容到粘贴板
    pyperclip.copy(msg)
    # 模拟键盘 ctrl + v 粘贴内容Z
    pyautogui.hotkey('ctrl', 'v')
    # 发送消息
    pyautogui.press('enter')


def send_msg(friend):
    # Ctrl + alt + w 打开微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    # 搜索好友
    pyautogui.hotkey('ctrl', 'f')
    # 复制好友昵称到粘贴板
    pyperclip.copy(friend)
    # 模拟键盘 ctrl + v 粘贴
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # 回车进入好友消息界面
    pyautogui.press('enter')
    # 一条一条发送消息
    for msg in get_msg():
        send(msg)
        # 每条消息间隔 2 秒
        time.sleep(2)


friend_names = ["文件传输助手"]  # 好友列表 ，给自己的微信好友好信息
for friend_name in friend_names:
        send_msg(friend_name)
print("ok")