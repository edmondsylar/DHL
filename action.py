import xlrd
from db import make_insertion

class DHL:
    def __init__(self, file):

        self.return_msg = ""

        self.loc = file

        self.wb = xlrd.open_workbook(self.loc)
        self.sheet = self.wb.sheet_by_index(0)

        self.serial = self.sheet.cell_value(1, 22)
        self.required = ['Sales Document', 'Delivery Number', 'Plant', 'Sold-to party', 'Created on', 'Material', 'Material Description', 'Order Quantity', 'Carrier', 'status']

        self.cols = []

        self.get_col_names()
        self.itter_data()

    def get_col_names(self):
        for i in range(59):
            self.col = self.sheet.cell_value(0, i)
            # print (col, i)
            self.cols.append({self.col:i})

    def itter_data(self):
        try:
            object_data ={}
            # for i in range(3):
            for i in range(self.sheet.nrows):
                for each in self.cols:
                    for key, value in each.items():
                        if key in self.required:
                            # print('{} : {}\n'.format(key, sheet.cell_value(i, value)))
                            object_data[key] = self.sheet.cell_value(i, value)
                # print (object_data, '\n\n')
                make_insertion(object_data)
            self.return_msg = "file uploaded"
        except Exception as error:
            self.return_msg = error
            # return (self.return_msg)


    def res(self):
        return (self.return_msg)
