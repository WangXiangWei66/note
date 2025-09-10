# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import cv2
v=cv2.VideoCapture(0) # 调用本机影响头

f,img=v.read() #读取图像
cv2.imwrite('my-pic/alxiao.jpg',img) # 保存成图片
#cv2.destroyAllWindows() # 用来删除窗口的，（）里不指定任何参数，则删除所有窗口
#文件 my-pic中产生
