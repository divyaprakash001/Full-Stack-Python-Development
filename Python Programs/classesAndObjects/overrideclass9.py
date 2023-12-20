class A:
    def __init__(self):
        print('class A constructor called')
        self.a=20
    
    
class B(A):
    def __init__(self):
        print('class B constructor called')
        self.a=30
        A.__init__(self)
    
    def disp(self):
        print('value of a=',self.a)
       


x = B()
x.disp()



