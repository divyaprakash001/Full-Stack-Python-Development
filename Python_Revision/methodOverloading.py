class Overloading:
    def __init__(self):
        print("this is constructor of overloading class")
    def __init__(self,a): #method overloading doesnot work here
        print("this is parameterised constructor of overloading class",a)
    
x = Overloading(7)