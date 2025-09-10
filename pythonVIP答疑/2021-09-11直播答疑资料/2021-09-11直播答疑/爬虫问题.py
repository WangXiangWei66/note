# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import tkinter as tk
import requests
from bs4 import BeautifulSoup
import urllib.parse as parse
from tkinter import messagebox as msg
import tkinter.filedialog as file

# my_window=tk.Tk()
# count=tk.StringVar()
# def func():
#     # reset
#     # my_label.config(text=count.get())
#     # count.set(my_lbox.get(my_lbox.curselection()))
#     # tk.messagebox
#     msg.showerror(title="hello....",message="hahahaha")
# # window
# my_window.geometry("200x130")
# # label
# my_label=tk.Label(my_window,text="........",bg="yellow",font=("微软雅黑",11),width=20,height=1)
# # # entry -- textbox
# # # show  -- passwordChar
# # my_entry = tk.Entry(my_window,show=None)
# # # button
# # command -- Listener --Event
# my_button=tk.Button(my_window,textvariable=count,bg="red",command=func)
# # listbox
# # lst =tk.StringVar()
# # arr=[1,3,4,7,8,6]
# # lst.set(arr)
# # my_lbox=tk.Listbox(my_window,listvariable=lst)
# # my_lbox.insert(2,"hello")
# # my_lbox.delete(4)
# # radio button
# my_rbtn=tk.Radiobutton(my_window,text="OP1",variable=count,value="a",command=func)
# my_rbtn.pack()
# # add to window
# my_label.pack()
# # my_entry.pack()
# # # my_lbox.pack()
# my_button.pack()
# # disp
# my_window.mainloop()

def login():
    global word
    fetch=word.get()
    fetch_html(fetch)

def fetch_html(kw):
    code=parse.quote(kw)
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    resp=requests.get(f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7978533205520407048&ipn=rj&ct=201326592&is=&fp=result&queryWord={code}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={code}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&nojc=&pn=30&rn=30&gsm=1e&1631362816757=",headers=headers)
    bs=BeautifulSoup(resp.content,"html.parser")
    print(bs)

# 窗口
login_window=tk.Tk()
# 登录窗口标题
login_window.title("更换壁纸")
# 登录窗口大小
login_window.geometry("600x400")
# 标签
lb_kw=tk.Label(login_window,text="爬取关键词",font=("微软雅黑",11),width=20).place(x=20,y=30)
# 输入框
word=tk.StringVar()
key=tk.Entry(login_window,width=40,textvariable=word).place(x=200,y=40)
# 按钮
btn=tk.Button(login_window,text="选择图片",font=("微软雅黑",13),width=40,command=login).place(x=70,y=70)

# 显示登录窗口
login_window.mainloop()