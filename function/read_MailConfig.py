import os
import codecs
import configparser




class Read_MailConfig:
    def __init__(self):
        self.ConfigPath = "D:\pyrequest-master\config\\MailConfig.ini"
        self.cf = configparser.ConfigParser()
        self.cf.read(self.ConfigPath)

    # return all section
    def getSection(self):
        secs = self.cf.sections()
        print('sections:', secs)
        return secs

    def getOption(self):
        opts = self.cf.options("EMAIL")
        print('options:', opts)
        return opts

    def getAll(self):
        kvs = self.cf.items("EMAIL")
        print('EMAIL:', kvs)
        return kvs

    #  定义方法，修改config分组下指定name的值value
    def setConfigValue(self, name, value):
        cfg = self.cf.set("config", name, value)
        fp = open(self.ConfigPath, 'w')
        cfg.write(fp)


    def get_email(self,name):
        value = self.cf.get("EMAIL", name)
        return value

mail = Read_MailConfig()
port = mail.get_email(name="mail_port")
server = mail.get_email(name="mailserver")
from_ = mail.get_email(name="from_")
to_ = mail.get_email(name="to_")
pwd = mail.get_email(name="pwd")

