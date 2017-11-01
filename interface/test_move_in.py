#coding:utf-8

import os
import sys
import requests
from function.myunit import Mytest
from function.Read_csv_for_url import URL
from JsonMesssgeTemplate.JsonParameter_Get import Json_Parameter_Get
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)



class move_in_test(Mytest):


    def test_par_all(self):
        ''' 所有参数正常时接口返回测试 '''
        r = requests.post(URL.move_in_url,json=Json_Parameter_Get.get_move_in()[0])
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result["isSuccess"],True )



if __name__ == "__main__":
    move_in_test()