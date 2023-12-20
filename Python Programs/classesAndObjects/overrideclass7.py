class A:
    def accept(self,a):
        print('A accept call')
        self.a=a
    def displ(self):  #overriden method
        print('value of a in class A: ',self.a)
    
class B(A):
    def accept(self,b,c):
        print('B accept call')
        self.b=b
        self.c=c
        A.accept(self,50)
    
    def displ(self):  #overriding method
        print('value of a in class B: ',self.a)
        print('value of b in class B: ',self.b)
        print('value of c in class B: ',self.c)
        A.displ(self)


x = B()    
# x.accept(2,3)
# x.displ()
# A.accept(x,12)
# A.displ(x)
# A.accept(B(),20)
# A.displ(B())
A.accept(x,20)
A.displ(x)



