#coding:utf-8

import unittest


class Mytest(unittest.TestCase):

    def setUp(self):
        print (u"测试开始！")



    def tearDown(self):
        print (u"测试结束！")
