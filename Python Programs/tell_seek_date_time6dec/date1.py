import datetime as d
# print(d.datetime.date(2023, 12, 6))
# print(d.datetime.today())
# print(d.datetime.now())

p=d.datetime.now()
print(p)
print(p.date())
print(p.date().month)
print(p.date().year)
print('------------')
print(p.time())
print(p.month)
print(p.year)
print('------------')
print(p.date().strftime('%d'))
print(p.date().strftime('%d-%m'))
print(p.date().strftime('%d-%m-%y'))
print(p.date().strftime('%d-%m-%y,%H:%M:%S'))  #here p.date() give date so there is no time available so print 00
print('------------')
print(p.strftime('%d-%m-%y'))
print(p.strftime('%H'))
print(p.strftime('%M'))
print(p.strftime('%S'))
print(p.strftime('%H:%M:%S'))
print('------------')
print(p.strftime('%Y-%m-%d'))  #capital Y means years print in 4 digits
print(p.strftime('%y-%m-%d'))  #small y means year print in 2 digits
print('------------')
print(p.strftime('%W')) #week of the year
print(p.strftime('%X')) 
print(p.strftime('%c')) 
# print(p.strftime('%Z')) #check how it work
print(p.strftime('%B')) 


