#coding:utf-8

class  Parameter_create_sku():

#放入json格式的参数由case进行调用
    #创建商品信息
    # --参数全


    create_sku = [
    {
        "key": "CP_1508986003534",
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
    #参数为空
    create_sku_null = [
     {
         "key": "CP_1508986003534",
         "orgId":'' ,
         "orgCode": "",
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
                 "uomCode": "",
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
                 "uomCode": "",
                 "uomBarCode": "",
                 "uomDescr": "EA",
                 "uomQty": 1,
                 "length": 0,
                 "width": 0,
                 "height": 0,
                 "weight": 0
             },
             {
                 "packageCode": "12135420",
                 "uomCode": "",
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
                 "uomCode": "",
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

    create_sku_wrong = [
     {
         "key": "testcase",
         "orgId":111111111 ,
         "orgCode": "testcase",
         "whId": 109455,
         "whCode": "testcase",
         "customerId": 111,
         "customerCode": "testcase",
         "skuId": 111111,
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
                 "uomCode": "",
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
                 "uomCode": "",
                 "uomBarCode": "",
                 "uomDescr": "EA",
                 "uomQty": 1,
                 "length": 0,
                 "width": 0,
                 "height": 0,
                 "weight": 0
             },
             {
                 "packageCode": "12135420",
                 "uomCode": "",
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
                 "uomCode": "",
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


    create_sku_less = [
        {

            "orgId": 111111111,
            "orgCode": "testcase",
            "whId": 109455,
            "whCode": "testcase",
            "customerId": 111,
            "customerCode": "testcase",
            "skuId": 111111,
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
                    "uomCode": "",
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
                    "uomCode": "",
                    "uomBarCode": "",
                    "uomDescr": "EA",
                    "uomQty": 1,
                    "length": 0,
                    "width": 0,
                    "height": 0,
                    "weight": 0
                },
                {
                    "packageCode": "12135420",
                    "uomCode": "",
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
                    "uomCode": "",
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