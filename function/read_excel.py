#conding:utf-8
import xlrd
from test_myself.setattr001 import a
from test_myself.a_json import JsonMessage

file = "D:\pyrequest-master\data\excel\sku.xlsx"


def read_excel(row_id,col_id):
    #查看工作表数量
    data = xlrd.open_workbook("D:\pyrequest-master\data\excel\sku.xlsx")
    sheet1_name = data.sheet_names()[0]

    #查看工作表1中的行，列个数
    sheel_1 = data.sheet_by_name("Sheet1")
    print(sheel_1.name,sheel_1.nrows,sheel_1.ncols)
    #打印出第几列和第几行的值
    print(sheel_1.col_values(1),sheel_1.row_values(1))
    #读取具体的某行某列的值
    print(sheel_1.cell(row_id,col_id).value)
    print(sheel_1.cell_value(1,0))
    print(sheel_1.row(1)[0].value)


def excel_table_byname(file=file ,colnameindex=0,by_name=u'Sheet1'):
    data = xlrd.open_workbook(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    print(list)

    jsonlist = []
    for json in list:
        b=a()
        b.setKey(json["key"])
        b.setOrgId(json["orgId"])
        jsonlist.append(b)

    c = JsonMessage()
    print(c.create_sku(jsonlist[0].getKey(),jsonlist[0].getOrgId()))



if __name__ == '__main__':
    excel_table_byname()
