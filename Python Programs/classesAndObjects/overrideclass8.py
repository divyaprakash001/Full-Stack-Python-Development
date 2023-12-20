class A:
    def displ(self,a):  
        self.a=a
        print('value of a in class A: ',self.a)
    
class B(A):
    def displ(self,a,b):
        self.a=a
        self.b=b  
        print('a=',self.a,'b=',self.b)
       


x = B()
A.displ(x,12)
x.displ(23,30)



