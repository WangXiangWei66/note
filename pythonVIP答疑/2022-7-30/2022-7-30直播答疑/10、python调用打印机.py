# coding:utf-8
# author:杨淑娟
import win32api
import os
if __name__ == '__main__':
    # 被注释掉的代码，是一个批量打印的操作
    # path=input('请输入文件夹的绝对路径:')
    # files=[path+'\\'+i for i in os.listdir(path)]
    # for filename in files:
    #     print(filename)
    #     win32api.ShellExecute(
    #         0,'print',filename,None,'.',0
    #     )


    # 以下三句代码就可以使用python调用打印机（默认打印机
    filename='d:/pythonpro/2022-7-30直播答疑/a.xlsx'

    win32api.ShellExecute( 0,'print',filename,None,'.',0)
    #
    print('完成')