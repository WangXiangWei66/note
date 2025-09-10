#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/5/2 23:30i
import pygame
import sys
pygame.init()
size=width,height=640,480
print(type(size))
screen=pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

pygame.quit()