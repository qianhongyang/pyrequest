#coding:utf-8

import requests

r = requests.get('https://github.com')

print(r.status_code)

path.append('./interface')
path = unittest.defaultTestLoader.discover('../interface',pattern = '*_test.py')
runner.run(path)