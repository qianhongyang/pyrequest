#coding:utf-8

import os
import time




#=====查找测试报告目录，找到最新生成的测试报告文件=========
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new








