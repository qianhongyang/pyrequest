#coding:utf-8

import smtplib
import time
from email.header import Header
from email.mime.text import *
from function import  read_MailConfig
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


#=======定义发送邮件================
def send_mail(file, from_, to_, pwd):
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'now' + 'result.html'
    # 插入附件
    att = MIMEMultipart()
    part = MIMEApplication(open(file, 'rb').read())
    part["Content-Type"] = 'application/octet-stream'
    part["Content-Disposition"] = 'attachment; filename=%s.html'%(now)
    att.attach(part)

    f = open(file, 'rb')
    mail_body = f.read()
    f.close()
    att.attach(MIMEText(mail_body, 'html', 'utf-8'))
    att['Subject'] = Header("自动化测试报告", "utf-8")
    att["From"] = from_
    att["To"] = to_



    smtp = smtplib.SMTP_SSL(read_MailConfig.server,read_MailConfig.port)
    smtp.login(from_, pwd)
    smtp.sendmail(from_, to_, att.as_string())
    smtp.quit()
    print('Email has send out')

