import datetime as d
import os
import time as t

cdate = d.datetime.now()
mydate = cdate.strftime('%Y') + '\\' + cdate.strftime('%b') + "\\" + cdate.strftime('%U') +'Week'+ "\\" + cdate.strftime('%d')
print(mydate)

os.chdir('Python Programs\\11Dec')

print(os.getcwd())

for i in range(31):
    if not os.path.exists(mydate+str(i+1)):
      os.makedirs(mydate + str(i+1))
    t.sleep(2)

for i in range(31):
    os.chdir(mydate)
    for l in os.listdir():
        print(l)

