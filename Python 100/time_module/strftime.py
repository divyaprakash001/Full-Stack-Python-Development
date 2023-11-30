import time
t = time.localtime()
formatted_time1 = time.strftime('%Y-%m-%d %H:%M:%S',t)
formatted_time2 = time.strftime('%d-%m-%Y %H:%M:%S',t)
print(formatted_time1)
print(formatted_time2)