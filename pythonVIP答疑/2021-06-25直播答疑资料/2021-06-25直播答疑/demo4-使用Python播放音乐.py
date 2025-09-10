#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import time
import pygame  # 第三方模块，pygame用于做游戏 ，需要安装，pip install pygame

pygame.init()  #  初始化方法
print("播放音乐1")
track = pygame.mixer.music.load(r"青花瓷.mp3") # 加载音乐文件

pygame.mixer.music.play() # 播放
time.sleep(10)
pygame.mixer.music.stop() # 停止