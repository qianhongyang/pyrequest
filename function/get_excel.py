import xlrd


class readExcel(object):

    def __init__(self, path):
        self.path = path

    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    def getRows(self):
        # 获取行数
        row = self.getSheet().nrows
        return row

    def getCol(self):
        # 获取列数
        col = self.getSheet().ncols
        return col
    # 以下是分别获取每一列的数值

    def getKey(self):
        TestName = []
        for i in range(1, self.getRows()):
            TestName.append(self.getSheet().cell_value(i, 0))
        return TestName

    def getOrgid(self):
        TestData = []
        for i in range(1, self.getRows()):
            TestData.append(self.getSheet().cell_value(i, 1))
        return TestData

    def getorgcode(self):
        TestUrl = []
        for i in range(1, self.getRows()):
            TestUrl.append(self.getSheet().cell_value(i, 2))
        return TestUrl

    def getwhid(self):
        TestMethod = []
        for i in range(1, self.getRows()):
            TestMethod.append(self.getSheet().cell_value(i, 3))
        return TestMethod

    def getwhcode(self):
        TestUid = []
        for i in range(1, self.getRows()):
            TestUid.append(self.getSheet().cell_value(i, 4))
        return TestUid

    def getcust(self):
        TestCode = []
        for i in range(1, self.getRows()):
            TestCode.append(self.getSheet().cell_value(i, 5))
        return TestCode