''' factorial
factorial(7) = 7*6*5*4*3*2*1
factorial(6) = 6*5*4*3*2*1
factorial(5) = 5*4*3*2*1
factorial(4) = 4*3*2*1
 '''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

# fibonacci sequence
def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(8))