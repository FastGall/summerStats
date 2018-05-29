import xlrd, xlwt
import matplotlib.pyplot as plt
#Open xls
print("print xls-file name")
name_xls = str(input())
rb = xlrd.open_workbook(name_xls,formatting_info=True)

#active page
sheet = rb.sheet_by_index(0)

employee = []
money_employee = []
salary_employee = []
all_money = 0
all_salary = 0
pure_money = 0


for i in range(sheet.nrows - 1):
    if(sheet.row_values(i+1)[4] not in employee):
        employee.append(sheet.row_values(i+1)[4])
        money_employee.append(int(sheet.row_values(i+1)[3]))
    else:
        for j in range(len(employee)):
            if(sheet.row_values(i+1)[4] == employee[j]):
                money_employee[j] +=  int(sheet.row_values(i+1)[3])

salary_employee = [500 for i in range(len(employee))]

for i in range(len(employee)):
    if(money_employee[i] >= 5000):
        salary_employee[i] += 500

for i in range(len(money_employee)):
    all_money += money_employee[i]
    all_salary += salary_employee[i]

pure_money = all_money - all_salary

for i in range(len(employee)):
    print(employee[i], money_employee[i], salary_employee[i])


print(all_money,pure_money)


plt.figure(figsize=(15,10))

explode = [0 for i in range(len(employee))]

plt.subplot(aspect=True)
plt.pie(money_employee, labels = employee, explode = explode, autopct = '%.2f%%', shadow=False);
plt.title("City statistic")

plt.show()
    