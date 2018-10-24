import xlrd
import datetime

data = xlrd.open_workbook('fundValue_2018.xls')
table = data.sheets()[0]

times = table.row_values(0)

length= len(times)
total_num = 0
i = 0
increase = 0

for time in times:
    week_num = datetime.datetime.strptime(time, "%Y-%m-%d").strftime("%w")
    if week_num == '5':
        total_num = total_num + 1
        if (length>i+1) and (float(table.cell(2, i).value) - float(table.cell(2, i + 1).value) > 0):
            increase = increase + 1
    i = i + 1

print('共有这么多个周五:%d'%total_num)
print('周五中股市上涨的天数：%d'%increase)