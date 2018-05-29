import xlrd, xlwt
print("Введите название для генерируемой таблицы")
name_xls = str(input())

wb = xlwt.Workbook()
print("Введите название листа таблицы")
current_day = str(input())
ws = wb.add_sheet(current_day)
ws.write(0, 0, 'Day')
ws.write(0, 1, 'Model')
ws.write(0, 2, 'Time')
ws.write(0, 3, 'Money')
ws.write(0, 4, 'Employee')
wb.save(name_xls)