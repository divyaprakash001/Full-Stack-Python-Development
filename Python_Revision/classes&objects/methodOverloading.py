class Overloading:
    def __init__(self):
        print("this is constructor of overloading class")
    def __init__(self,a): #method overloading doesnot work here
        print("this is parameterised constructor of overloading class",a)
    def disp(self):
        print("this is zero parameter method")
    def disp(self,a):
        a=a
        print("this is one parameter method",a)
    def disp(self,a,b):
        a=a
        b=b
        print("this is two parameter method",a,b)
    
x = Overloading(7)
x.disp(2,3)