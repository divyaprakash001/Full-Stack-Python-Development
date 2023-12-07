import datetime

# datetime is a module in which date is a class
# here we are calling constructor of date class date(cls,year,month,day)
p = datetime.date(2023,12,7)
print('Date passed as argument is',p)

current_date1 = datetime.date.today()
current_date2 = datetime.datetime.now()
print('Today\'s date is', current_date1)
print('Today\'s date time is', current_date2)

print(current_date1.year)
print(current_date1.month)
print(current_date1.day)
print('--------------')


# getting date from timestamp
dtime = datetime.datetime.fromtimestamp(1700739999)
print(dtime)

# convert date object to string
strdate =datetime.date.isoformat(current_date1)
print(strdate,type(strdate))


print(datetime.date.isocalendar(current_date1))
# print(datetime.date.fromordinal(720282))
print(datetime.date.isoweekday(current_date1))