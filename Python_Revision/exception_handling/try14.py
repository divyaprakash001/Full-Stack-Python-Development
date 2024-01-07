def bool_func():
    try:
      raise KeyboardInterrupt 
    finally: #if finally contain return, break,continue, no error raise at try clause
     return False
    
print(bool_func())

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
       print('zero error')
    else:
       print("the result is",result)
    finally:
       print("executing finally clause")

# divide(10,2)
# divide(10,0)
divide('10','0')