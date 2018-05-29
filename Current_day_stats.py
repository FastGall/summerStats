from xlrd import open_workbook
from xlutils.copy import copy
print("Введите название Exel-таблицу, в которую будут добавляться данные")
name_xls = str(input())
rb = open_workbook(name_xls)
wb = copy(rb)

read = rb.sheet_by_index(0)
sheet = wb.get_sheet(0) # Работа в текущем Exel-листе
print("[Day,Model,Time,Money,Employee]")
current_list = str(input())
current_list = current_list.split(',')
j = 0
if(len(current_list) != 5):
    print("Error input")
    exit()
while(1):
    for i in range(len(current_list)):
        sheet.write(read.nrows + j, i, current_list[i])
    print("Еще? Д/н")
    n = input()
    if(n == 'н'):
        break
    print("[Day,Model,Time,Money,Employee]")
    current_list = str(input())
    current_list = current_list.split(',')
    j+=1

wb.save(name_xls)