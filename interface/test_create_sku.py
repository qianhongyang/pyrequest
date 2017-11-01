#coding:utf-8

import os
import sys
import unittest
import requests

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from function.myunit import Mytest
from function.Read_csv_for_url import URL
from JsonMesssgeTemplate.JsonParameter_Get import Json_Parameter_Get


class creat_sku_test(Mytest):


    def test_par_all(self):
        ''' 所有参数正常时接口返回测试 '''
        r = requests.post(URL.create_sku_url, json=Json_Parameter_Get.get_creat_sku()[0])
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result["isSuccess"], True)

    def test_par_null(self):
        """必填参数为空时接口返回测试"""
        r = requests.post(URL.create_sku_url, json=Json_Parameter_Get.get_creat_sku()[1])
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result["isSuccess"], False)
        self.assertIn('orgCode=不能为空',self.result['errorMsg'])
        self.assertIn('orgId=不能为null',self.result['errorMsg'])

    def test_par_wrong(self):
        """必填参数填写错误接口返回测试"""
        r = requests.post(URL.create_sku_url, json=Json_Parameter_Get.get_creat_sku()[2])
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result["isSuccess"], False)
        self.assertIn('数据提交失败', self.result["errorMsg"])

    def test_par_less(self):
        """必填参数少传接口返回测试"""
        r = requests.post(URL.create_sku_url,json=Json_Parameter_Get.get_creat_sku()[3])
        self.result = r.json()
        print(self.result)
        self.assertIn('key=不能为空',self.result["errorMsg"])


if __name__ == '__main__':
    creat_sku_test()
