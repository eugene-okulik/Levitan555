import datetime

date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
human_month = datetime.datetime.strftime(python_date, '%B')
human_date = datetime.datetime.strftime(python_date, '%d.%m.%Y, %H:%M')

print(human_month)
print(human_date)
