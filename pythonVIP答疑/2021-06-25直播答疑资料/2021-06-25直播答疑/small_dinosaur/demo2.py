#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/5/2 22:56
import pygame                         # 将pygame库导入到Python程序中
from pygame.locals import  *          #导入pygame中的常量
SCREENWIDTH=822                       #窗体宽度
SCREENHEIGHT=260                      #窗体高度
FPS=30



#更新画面的时间

def mainGame():
    score=0                           #得分
    over=False
    global SCREEN,FPSCLOCL
    pygame.init()                    #初始化pyage
    #使用pygame时钟之前，必须先创建Clock对象的一个实例
    #控制每个循环多长时间运行一次
    FPSCLOCL=pygame.time.Clock()
    #创建一个窗体，方便我们与程序的交互
    SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('小恐龙')    #设置窗体标题

    while True:
        # 判断是否单击了关闭窗体
        for event in pygame.event.get():
            # 如果单击了关闭窗体就将窗体关闭
            if event.type == QUIT:
                exit()  # 关闭窗体
        pygame.display.update()  # 更新整个窗体
        FPSCLOCL.tick(FPS)  # 循环应该多长时间运行一次


if __name__ == '__main__':
    mainGame()

#