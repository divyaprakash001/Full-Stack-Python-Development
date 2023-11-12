# default arguments
def greet(fname,mname='prakash',lname='yadav'):
    print("Hello",fname,mname,lname)

greet('Divya',lname='Yadav',mname='Prakash')

# variable length arguments
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print("The average of the numbers :: ",sum/len(numbers))

average(1,2)

# keyword arbitrary arguments

def greeting(**name):
    print(type(name))
    print("Hello,",name['fname'],name['lname'],name['mname'])

greeting(fname='divya',lname='yadav',mname='prakash')

def dedo(name):
    return name+' hai'
    return name

print(dedo('divya'))