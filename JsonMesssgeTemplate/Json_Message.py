



class JsonMessage:
#--------------------------创建商品接口json模板----------------------
    def create_sku(self,key,orgId,orgCode,whId,whCode,customerId,customerCode,skuId,skuCode,descrCn,packageCode,uomCode):
        create_sku_json = [
            {
                "key": key,
                "orgId": orgId,
                "orgCode": orgCode,
                "whId": whId,
                "whCode": whCode,
                "customerId": customerId,
                "customerCode": customerCode,
                "skuId": skuId,
                "skuCode": skuCode,
                "descrCn": descrCn,
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
                        "packageCode": packageCode,
                        "uomCode": uomCode,
                        "uomBarCode": "4891599338393",
                        "uomDescr": "EA",
                        "uomQty": 1,
                        "length": 0,
                        "width": 0,
                        "height": 0,
                        "weight": 0
                    },
                    {
                        "packageCode": packageCode,
                        "uomCode": uomCode,
                        "uomBarCode": "4891599338393",
                        "uomDescr": "EA",
                        "uomQty": 1,
                        "length": 0,
                        "width": 0,
                        "height": 0,
                        "weight": 0
                    },
                    {
                        "packageCode": packageCode,
                        "uomCode": uomCode,
                        "uomBarCode": "4891599338393",
                        "uomDescr": "箱",
                        "uomQty": 24,
                        "length": 40,
                        "width": 26,
                        "height": 12,
                        "weight": 8.4
                    },
                    {
                        "packageCode": packageCode,
                        "uomCode": uomCode,
                        "uomBarCode": "4891599332223",
                        "uomDescr": "箱",
                        "uomQty": 24,
                        "length": 40,
                        "width": 26,
                        "height": 12,
                        "weight": 8.4
                    },
                    {
                        "packageCode": packageCode,
                        "uomCode": uomCode,
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
        return create_sku_json
#--------------------------移入接口json模板----------------------
    def  move_in(self,orgId,orgCode,whId,whCode,moveNo,key):
        move_in = [{
	"orgId": orgId,
	"orgCode": orgCode,
	"whId": whId,
	"whCode":whCode ,
	"customerId": 1244835,
	"customerCode": "LH",
	"key": key,
	"moveHeaderId": 1000031,
	"moveNo": moveNo,
	"createdTime": "2016-07-18 15:46:05",
	"skuId": 33331,
	"skuCode": "33331",
	"moveQtyUom": 100,
	"fixCreatedTime": "2015-05-01 00:00:00",
	"fixExpiredTime": "2020-04-30 00:00:00",
	"fixStatusId": 448716,
	"lotHeaderId": 467505,
	"lotAtt02": "B2C",
	"fromLpnCode": "112",
	"moveDetailId":214748364895

}]
        return move_in