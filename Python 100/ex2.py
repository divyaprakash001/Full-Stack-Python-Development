# greet goodmorning sir as according to the present time

import time as t

# print(t.localtime().tm_hour)

timestap2 = t.strftime('%H:%M:%S')
print(timestap2)
hour= int(t.strftime('%H'))
print(hour)
print(type(hour))
t3= t.strftime('%M')
print(t3)
t4= t.strftime('%S')
print(t4)

if hour>=0 and hour<12:
    print('good morning')
elif hour >= 12 and hour < 17:
    print('good evening')
elif hour>=17 and hour<0:
    print('good night')