#coding:utf-8

import csv

class URL():


        filename = 'D:\pyrequest-master\config\\base_url.csv'

        file = open(filename,'r')
        date = csv.DictReader(file)


        # next(date_name)
        # for i in date_name:
        #     print(i)

        dict={}
        for i  in date :
            # if line1['name'] == '创建商品':
            #     print (line1)
            ip = i.get('ip')
            port = i.get('port')
            url = i.get('url')
            #创建商品接口的url
            url = 'http://'+ip+':'+port+url
            name = i.get('name')
            #print(name)
            # print(type(url))
            #print(url)
            dict[name]=url
        for key in dict:

            create_sku_url = str(dict["创建商品"])
            move_in_url = str(dict["移入"])
            order_create_url = str(dict["订单创建"])
            transferoutbill_create_url = str(dict["移出"])
            order_cancel_url = str(dict["订单取消"])
            reconciliation_pull_url = str(dict["库存对账"])



if __name__ == '__main__':
    URL()