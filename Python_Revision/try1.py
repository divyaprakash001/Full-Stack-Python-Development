try:
    print("hllo world")
    print(10/0)
except(NameError,TypeError,ArithmeticError) as e:
    print('soemthing got error',e)

try:
    print("hello world")
    print(10/0)
except(NameError) as n:
    print('soemthing got error',n)
except(TypeError) as t:
    print('soemthing got error',t)
except ZeroDivisionError as z:
    print('zero error',z)
except(ArithmeticError) as a:
    print('soemthing got error',a)