def calculate(a,b):
    print(a/b)

try:
    calculate(10,0)
except ZeroDivisionError as z:
    print(f'The error is {z}')
else:  #is no error then this will execute
    print('else => if no error then this will execute')
finally:
    print("finlly execute all time")