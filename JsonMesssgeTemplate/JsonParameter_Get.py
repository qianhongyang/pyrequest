#coding:utf-8
from JsonMesssgeTemplate.JsonMessageParameter import SetParameter
from JsonMesssgeTemplate.Json_Message import JsonMessage
from function.read_excel import excel_by_list
from function import read_HostConfig

sku_path = read_HostConfig.sku_path
move_in_path = read_HostConfig.move_path
class Json_Parameter_Get():


    def get_creat_sku():
        jsonlist = []
        for json in excel_by_list(sku_path):
            CreateSkuPar = SetParameter()
            CreateSkuPar.setKey(json["key"])
            CreateSkuPar.setOrgId(json["orgId"])
            CreateSkuPar.setCustomerCode(json["customerCode"])
            CreateSkuPar.setCustomerId(json["customerId"])
            CreateSkuPar.setDescrCn(json["descrCn"])
            CreateSkuPar.setWhId(json["whId"])
            CreateSkuPar.setWhCode(json["whCode"])
            CreateSkuPar.setSkuId(json["skuId"])
            CreateSkuPar.setSkuCode(json["skuCode"])
            CreateSkuPar.setPackageCode(json["packageCode"])
            CreateSkuPar.setUomCode(json["uomCode"])
            CreateSkuPar.setOrgCode(json["orgCode"])
            jsonlist.append(CreateSkuPar)

        a = JsonMessage()
        caselist = []
        for i in range(0,len(jsonlist)):
            case = a.create_sku(jsonlist[i].getKey(), jsonlist[i].getOrgId(), jsonlist[i].getOrgCode(),
                              jsonlist[i].getWhId(),
                              jsonlist[i].getWhCode(), jsonlist[i].getCustomerId(), jsonlist[i].getCustomerCode(),
                              jsonlist[i].getSkuId(),
                              jsonlist[i].getSkuCode(), jsonlist[i].getDescrCn(), jsonlist[i].getPackageCode(),
                              jsonlist[i].getUomCode())
            caselist.append(case)
        return caselist

    def get_move_in():
        jsonlist = []
        for json in excel_by_list(move_in_path):
            CreateSkuPar = SetParameter()
            CreateSkuPar.setKey(json["key"])
            CreateSkuPar.setOrgId(json["orgId"])
            CreateSkuPar.setWhId(json["whId"])
            CreateSkuPar.setWhCode(json["whCode"])
            CreateSkuPar.setMoveNo(json["moveNo"])
            CreateSkuPar.setOrgCode(json["orgCode"])
            jsonlist.append(CreateSkuPar)

        a = JsonMessage()
        caselist = []
        for i in range(0,len(jsonlist)):
            case = a.move_in(jsonlist[i].getOrgId(), jsonlist[i].getOrgCode(),
                              jsonlist[i].getWhId(),
                              jsonlist[i].getWhCode(), jsonlist[i].getMoveNo(),jsonlist[i].getKey())
            caselist.append(case)
        return caselist




#
# if __name__ == "__main__":
#     a = Json_Parameter_Get()
#     a.get_creat_sku()