x = lambda a : a * 5
print(x(5))

x = lambda a, b : a*b
print(x(5,6))

x = lambda a,b: a*b if a>b else a+b
print(x(7,5))

x = lambda a,b : a/b if b==0 else a*b
print(x(4,5))

def myfunc(n):
    return lambda a : a * n

mydfunc = myfunc(2)
mydouble = mydfunc(11)
print('my double is',mydouble)

