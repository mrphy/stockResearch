import xlrd
import datetime

data = xlrd.open_workbook('fundValue_2018.xls')
table = data.sheets()[0]

times = table.row_values(0)

length= len(times)

set = []

st1 = datetime.datetime.strptime(times[0], "%Y-%m-%d")
i = 0
for time in times:
    if i != 0:
        st2 = datetime.datetime.strptime(time, "%Y-%m-%d")
        if (st1 - st2 != datetime.timedelta(days=1)):
            if(i!=length-1):
                set.append(i)
        st1 = st2
    i = i + 1

total = 0
diff_count = 0
before_holiday_count = 0
after_holiday_count = 0

for index in set:
    total = total + 1
    before_holiday = float(table.cell(2, index).value) - float(table.cell(2, index + 1).value)
    after_holiday = float(table.cell(2, index - 1).value) - float(table.cell(2, index).value)
    if (before_holiday > 0):
        before_holiday_count = before_holiday_count + 1
    if (after_holiday > 0):
        after_holiday_count = after_holiday_count + 1
    if (after_holiday * before_holiday < 0):
        diff_count = diff_count + 1

print('节假日总数：', total)
print('同涨同跌的比例：%.2f%%' % (100 * (1 - diff_count / total)))
print('节假日之前涨的比例: %.2f%%' % (100 * before_holiday_count / total))
print('节假日之后涨的比例: %.2f%%' % (100 * after_holiday_count / total))
