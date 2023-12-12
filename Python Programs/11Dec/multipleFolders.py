import datetime as d
import os
import time as t

os.chdir('Python Programs\\11Dec')

print(os.getcwd())

for i in range(20):
    path = f'Python_Tutorial/Tut{i+1}'
    if not os.path.exists(path):
      os.makedirs(path)
      t.sleep(1)


    



