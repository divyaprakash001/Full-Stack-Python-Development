def double(x):
    return x*2
print(double(5))

double2 = lambda x:x*2
print(double2(6))

avg = lambda x,y:(x+y)/2
print(avg(10,20))

# use of lambda function as an argument in function

def appl(fx,value):
    return 6+fx(value)

print(appl(lambda x: x*x*x,2))