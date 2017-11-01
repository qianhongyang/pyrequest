# def create_sku_json(self,key,orgId,orgCode,whId,whCode,packageCode,uomCode,uomBarCode):


class JsonMessage:
    def create_sku(self, key, orgId):
        create_sku_json = [
            {
                "key": key,
                "orgId": orgId,
                # "orgCode": orgCode,
                # "whId": whId,
                # "whCode": whCode,
                # "customerId": 111111,
                # "customerCode": "LH",
                # "skuId": 33332,
                # "skuCode": "33332",
                # "descrCn": "加多宝凉茶310ml*10罐/箱",
                # "grossWeight": 0.3458,
                # "netWeight": 0.34,
                # "cube": 520,
                # "skuLength": 1,
                # "skuWidth": 1,
                # "skuHigh": 1,
                # "skuEANCode": "4.8916E+12",
                # "skuEANCode2": "4.8916E+12",
                # "skuEANCode3": "4.8916E+12",
                # "packingQty": 24,
                # "isSpecialShape": "true",
                # "skuUomList": [
                #     {
                #         "packageCode": packageCode,
                #         "uomCode": uomCode,
                #         "uomBarCode": uomBarCode,
                #         "uomDescr": "EA",
                #         "uomQty": 1,
                #         "length": 0,
                #         "width": 0,
                #         "height": 0,
                #         "weight": 0
                #     },
                #     {
                #         "packageCode": "12135421",
                #         "uomCode": "EA",
                #         "uomBarCode": "4891599338393",
                #         "uomDescr": "EA",
                #         "uomQty": 1,
                #         "length": 0,
                #         "width": 0,
                #         "height": 0,
                #         "weight": 0
                #     },
                #     {
                #         "packageCode": "12135420",
                #         "uomCode": "CS",
                #         "uomBarCode": "CREATE USER 'walleadmin'@'localhost' ; ",
                #         "uomDescr": "箱",
                #         "uomQty": 24,
                #         "length": 40,
                #         "width": 26,
                #         "height": 12,
                #         "weight": 8.4
                #     },
                #     {
                #         "packageCode": "12135420",
                #         "uomCode": "CS",
                #         "uomBarCode": "4891599332223",
                #         "uomDescr": "箱",
                #         "uomQty": 24,
                #         "length": 40,
                #         "width": 26,
                #         "height": 12,
                #         "weight": 8.4
                #     },
                #     {
                #         "packageCode": "12135420",
                #         "uomCode": "QA",
                #         "uomDescr": "EA",
                #         "uomQty": 12,
                #         "length": 0,
                #         "width": 0,
                #         "height": 0,
                #         "weight": 0
                #     }
                # ]
            }
        ]
        return create_sku_json
