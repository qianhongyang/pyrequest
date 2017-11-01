#coding:utf-8

import configparser
import code
import os


class ReadConfig():
    def readconfig(self,path,secs,name):
        self.cf = configparser.ConfigParser()
        self.cf.read(path)
        value = self.cf.get(secs,name)
        return value

