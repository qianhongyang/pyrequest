import os
import codecs
import configparser




class Read_HostConfig:
    def __init__(self):
        self.ConfigPath = "D:\pyrequest-master\config\\HostConfig.ini"
        self.cf = configparser.ConfigParser()
        self.cf.read(self.ConfigPath)

    # return all section
    def getSection(self):
        secs = self.cf.sections()
        print('sections:', secs)
        return secs

    def getOption(self):
        opts = self.cf.options("HTTP")
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

    def get_host(self,name):
        value = self.cf.get("ExcelFilePath", name)
        return value

file = Read_HostConfig()
sku_path = file.get_host(name="sku_path")
move_path = file.get_host(name="move_in_path")

