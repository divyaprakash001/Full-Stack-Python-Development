import datetime as d
import os

cdate = d.datetime.now()
mydate = cdate.strftime('%Y') + '\\' + cdate.strftime('%b') + "\\" + cdate.strftime('%d')
print(mydate)
os.chdir('Python Programs\\11Dec')
print(os.getcwd())
if not os.path.exists(mydate):
    os.makedirs(mydate)
