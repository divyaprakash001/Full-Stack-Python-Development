class methodVar:
    staVar = 'static'
    def __init__(self):
        self.a=10
        self.b=20

    def method(self,a):
        m = a  #method scope variable
        print('the value of method var m is',m)
        print('the value of method var a is',a)


    def disp(self):
        print('The value of a is',self.a)
        print('The value of b is',self.b)
    
x = methodVar()
x.method(2)
x.c = 30
print('The value of c is',x.c)