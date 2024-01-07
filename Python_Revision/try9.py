try:
    a = 10
    b=0
    if b == 0:
        raise ZeroDivisionError('zero se divide nahi karna hai')
    else:
        print(f"the result is :: {a/b}")
except ZeroDivisionError as z:
    print(f"the error is ::  {z}")