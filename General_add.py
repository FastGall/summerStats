import xlrd, xlwt
from xlrd import open_workbook
from xlutils.copy import copy

print("print xls-file name for save")
name_xls = str(input())
rb = open_workbook(name_xls)
db = open_workbook('General.xls')
wb = copy(db)

read = rb.sheet_by_index(0)
read_db = db.sheet_by_index(0)
sheet = wb.get_sheet(0)

for i in range(read.nrows - 1):
    for j in range(5):
        sheet.write(read_db.nrows + i, j, read.row_values(i+1)[0])

wb.save('General.xls')

