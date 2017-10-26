#coding:utf-8

import os
import sys
import unittest
import requests

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from function.myunit import Mytest
from config.parameter_move_in import Parameter_move_in
from function.Read_csv_for_url import URL


class move_in_test(Parameter_move_in,Mytest):


    def test_par_all(self):
        ''' 所有参数正常时接口返回测试 '''
        r = requests.post(URL.move_in_url,json=Parameter_move_in.move_in_par_all)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result["isSuccess"], True)


if __name__ == "__main__":
    move_in_test()