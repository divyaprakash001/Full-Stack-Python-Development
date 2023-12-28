import time
import math

# decorator to calculate duration
# taken by any function
def calculate_time(func):

    def inner1(*args, **kwargs):

        begin = time.time()

        func(*args,**kwargs)

        end = time.time()

        print("Total time taken in : ",end - begin)
    
    return inner1

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(5)