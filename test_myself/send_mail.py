#coding:utf-8

import smtplib
import time
from email.header import Header
from email.mime.text import *
from function import  read_MailConfig
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from function import New_Report

from_ = "deanhongyang@foxmail.com "
to_ = "deanhongyang@foxmail.com"
pwd = "ffqpeobytofsbbge"

now = time.strftime("%Y-%m-%d %H_%M_%S")

test_report = "D:\pyrequest-master\data\\report\\"
new_report = New_Report.new_report(test_report)
# 插入附件
msg = MIMEMultipart()
part = MIMEApplication(open(new_report, 'rb').read())
part["Content-Type"] = 'application/octet-stream'
part["Content-Disposition"] = 'attachment; filename=%s.html'%(now)
msg.attach(part)

msg['to'] = to_
msg['from'] =from_
msg['CC']=to_
msg['subject'] = Header('冒烟测试结果')

f = open(new_report ,'rb')
mail_body = f.read()
f.close()
msg.attach(MIMEText(mail_body, "html",'utf-8'))

server = smtplib.SMTP_SSL("smtp.qq.com",465)
server.login(from_,pwd)
msg_text=msg.as_string()
server.sendmail(msg['from'], msg['to'],msg_text)
server.quit()
print("Email has been send")