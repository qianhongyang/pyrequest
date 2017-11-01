import json


create_sku = [
        {
            "key": "CP_1509337225032",
            "orgId": 100200,
            "orgCode": "BEST_SH_TAOBAO",
            "whId": 109455,
            "whCode": "SH_LJ_WH",
            "customerId": 1244835,
            "customerCode": "LH",
            "skuId": 33334,
            "skuCode": "33334",
            "descrCn": "加多宝凉茶310ml*10罐/箱",
            "grossWeight": 0.3458,
            "netWeight": 0.34,
            "cube": 520,
            "skuLength": 1,
            "skuWidth": 1,
            "skuHigh": 1,
            "skuEANCode": "4.8916E+12",
           "skuEANCode2": "4.8916E+12",
           "skuEANCode3": "4.8916E+12",
            "packingQty": 24,
            "isSpecialShape": "true",
            "skuUomList": [
                {
                    "packageCode": "12135420",
                    "uomCode": "EA",
                    "uomBarCode": "4891599331288",
                    "uomDescr": "EA",
                    "uomQty": 1,
                    "length": 0,
                    "width": 0,
                    "height": 0,
                    "weight": 0
                },
                {
                    "packageCode": "12135421",
                    "uomCode": "EA",
                    "uomBarCode": "4891599338393",
                    "uomDescr": "EA",
                    "uomQty": 1,
                    "length": 0,
                    "width": 0,
                    "height": 0,
                    "weight": 0
                },
                {
                    "packageCode": "12135420",
                    "uomCode": "CS",
                    "uomBarCode": "CREATE USER 'walleadmin'@'localhost' ; ",
                    "uomDescr": "箱",
                    "uomQty": 24,
                    "length": 40,
                    "width": 26,
                    "height": 12,
                    "weight": 8.4
                },
                {
                    "packageCode": "12135420",
                    "uomCode": "CS",
                    "uomBarCode": "4891599332223",
                    "uomDescr": "箱",
                    "uomQty": 24,
                    "length": 40,
                    "width": 26,
                    "height": 12,
                    "weight": 8.4
                },
                {
                    "packageCode": "12135420",
                    "uomCode": "QA",
                    "uomDescr": "EA",
                    "uomQty": 12,
                    "length": 0,
                    "width": 0,
                    "height": 0,
                    "weight": 0
                }
            ]
        }
    ]
b = {
	"orgId": 100200,
	"orgCode": "BEST_SH_TAOBAO",
	"whId": 279655,
	"whCode": "SH_EC_YHC",
	"customerId": 111111,
	"customerCode": "LH",
	"key": "Mo_1509337225120",
	"moveHeaderId": 1000031,
	"moveNo": "DDBH00000052",
	"createdTime": "2016-07-18 15:46:05",
	"skuId": 33332,
	"skuCode": "33332",
	"moveQtyUom": 101,
	"inboundTime":"" ,
	"fixCreatedTime": "2015-05-01 00:00:00",
	"fixExpiredTime": "2020-04-30 00:00:00",
	"fixStatusId": 448716,
	"lotHeaderId": 467505,
	"lotAtt01":"" ,
	"lotAtt02": "B2C",
	"lotAtt03": "",
	"lotAtt04": "",
	"lotAtt05": "",
	"lotAtt06": "",
	"fromLpnCode": "113",
	"susr1":"" ,
	"susr2":"" ,
	"susr3":"" ,
	"susr4":"" ,
	"susr5":"" ,
	"moveDetailId":214748364895

}
print(type(json.loads(b)))