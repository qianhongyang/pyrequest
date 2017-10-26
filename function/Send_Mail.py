#coding:utf-8

import smtplib
from email.header import Header
from email.mime.text import *





#=======定义发送邮件================
def send_mail(file, from_, to_, pwd):
        f = open(file, 'rb')
        mail_body = f.read()
        f.close()
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header("自动化测试报告", "utf-8")
        msg["From"] = from_
        msg["To"] = to_

        smtp = smtplib.SMTP_SSL("smtp.mxhichina.com", 465)

        smtp.login(from_, pwd)
        smtp.sendmail(from_, to_, msg.as_string())
        smtp.quit()
        print('Email has send out')

