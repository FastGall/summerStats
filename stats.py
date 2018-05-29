import xlrd, xlwt
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
import datetime as dt
import csv
#Open xls
print("xls-file Для статистики")
name_xls = str(input())
rb = xlrd.open_workbook(name_xls,formatting_info=True)

#active page
sheet = rb.sheet_by_index(0)

model = []
model_money = []

for i in range(sheet.nrows - 1):
    if(sheet.row_values(i+1)[1] not in model):
        model.append(sheet.row_values(i+1)[1])
        model_money.append(int(sheet.row_values(i+1)[3]))
    else:
        for j in range(len(model)):
            if(sheet.row_values(i+1)[1] == model[j]):
                model_money[j] += int(sheet.row_values(i+1)[3])

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.title('Диаграмма моделей')

ax = plt.axes()
ax.yaxis.grid(True, zorder = 1)

xs = range(len(model))
print("Введите дату, или период")
date = str(input())
plt.bar([x + 0.05 for x in xs], model_money,
        width = 0.2, color = 'red', alpha = 0.7, label = date,
        zorder = 2)
plt.xticks(xs, model)

fig.autofmt_xdate(rotation = 25)

plt.legend(loc='upper right')
plt.show()
#fig.savefig('bars.png')