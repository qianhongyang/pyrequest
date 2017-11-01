#coding:utf-8
from sys import  *
import time
from function.HTMLTestRunner import HTMLTestRunner
import unittest
path.append('../interface')
from function.Send_Mail import send_mail
from function import New_Report
from interface.test_create_sku import creat_sku_test
from interface.test_move_in import move_in_test
from function import read_MailConfig

class Run_tests:

    def __init__(self):
        print("-----------------------------开始测试！---------------------------------")
        # 添加测试套件
        self.suite = unittest.TestSuite()
        # 现在时间转字符串
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 测试报告命名
        self.filename = "D:\pyrequest-master\data\\report\\" + now + u'result.html'
        self.test_report = "D:\pyrequest-master\data\\report\\"


    def  suite_case(self):


        #执行所有测试案例
         #path = unittest.defaultTestLoader.discover('../interface',pattern = 'test_*.py')  #测试创建商品

        #创建商品接口
        self.suite.addTest(creat_sku_test("test_par_all"))                           #case - 创建商品时参数全
        self.suite.addTest(creat_sku_test("test_par_null"))                         #case - 创建商品时必填参数为空
        self.suite.addTest(creat_sku_test("test_par_wrong"))                        #case - 创建商品时参数填写错误
        self.suite.addTest(creat_sku_test("test_par_less"))                         #case -  创建商品时必填参数“key”不传

        #移入货物接口
        self.suite.addTest(move_in_test("test_par_all"))                            #case - 移入货物时参数全
        self.suite.addTest(move_in_test("test_par_null"))                            # case - 移入货物时参数为空
        self.suite.addTest(move_in_test("test_par_wrong"))                            # case - 移入货物时参数错误
        self.suite.addTest(move_in_test("test_par_less"))                            # case - 移入货物时必填参数不传

    def run_case(self):
        self.suite_case()
        fp = open(self.filename, 'wb')
        # 测试用例以报告形式执行
        self.runner = HTMLTestRunner(stream=fp, title='百世接口测试', description='用例执行情况')
        #runner = unittest.TextTestRunner()
        self.runner.run(self.suite)
        # 找到最新报告路径，发送最新报告
        fp.close()
        #调用方法，发送邮件
        new_report = New_Report.new_report(self.test_report)
        send_mail(new_report,read_MailConfig.from_,read_MailConfig.to_,read_MailConfig.pwd)
        print("----------------------------------case执行结束！-----------------------------------")

if __name__ == "__main__":
    Run_tests().run_case()
