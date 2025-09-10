# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#(1)导入模块
import smtplib
from  email.mime.text  import  MIMEText
#构建邮件头
from email.header import   Header
import schedule
import time
def job():
    #(2)创建STMP对象
    server=smtplib.SMTP()
    #server=smtplib.SMTP_SSL()
    #(3)连接服务器
    server.connect('smtp.qq.com',25)
    #(4)登录指定的服务器
    server.login('2954595560@qq.com','jaxkncsqtqkudhej')
    #群发接收人的QQ
    to_addrs=['2954595560@qq.com','68554698@qq.com','296626472@qq.com']
      #构建邮件内容 文本内容，文本类型，文本编码
    msg=MIMEText('PythonNB','plain','utf-8')
    msg['From']=Header('马士兵教育--程序员的创富地')
    msg['To']=Header(','.join(to_addrs))
    msg['Subject']=Header('人生苦短，你需要使用Python')
    #(5)发送邮件
    server.sendmail('2954595560@qq.com',to_addrs,msg.as_string())
    #(6)退出
    server.quit()
    print('邮件发送成功')
schedule.every(3).seconds.do(job)
while True:
   schedule.run_pending()
   time.sleep(1)