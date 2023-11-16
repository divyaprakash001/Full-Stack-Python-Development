# default argument
def calculate(a,b=10):
    print("The average is ",(a+b)/2)
    
calculate(10)

def greet(fname,mname='prakash',lname='yadav'):
    print("Hello, i am ",fname,mname,lname)

greet('divya')

# keyword argument
greet(fname='divya',lname='ahir',mname='prakash')


# variable length argumnent
def average(*numbers):  #here *numbers types is tuple
    print(type(numbers))
    l = len(numbers)
    sum=0
    for i in numbers:
        sum+=i
    print("The average is ",sum/l)

average(10,20,30,40,50)

# keyword arbitrary arguments
def greets(**name):
    print(type(name))
    print('Hello,',name['fname'],name['mname'],name['lname'])

greets(mname='prakash',lname='yadav',fname='divya')


def product(*numbers):
    pro = 1
    for i in numbers:
        pro*=i
    return pro

product = product(1,2,3,4,5)
print(product)

def findMiddle(s):
    m  = int(len(s)/2)
    fh = s[:m]
    sh= s[m:]
    if fh == sh:
        print('symetric')
    else:
        print("not sysmetric")

findMiddle('amaama')