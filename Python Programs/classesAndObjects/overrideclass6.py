class A:
    def accept(self,a,b):
        a = input('enter first number :: ')
        b = input('enter second number :: ')
        self.a=a
        self.b=b
        print(a)
        print(b)
    
class B(A):
     
     def accept(self,a,b,c):
        a = input('enter first number :: ')
        b = input('enter second number :: ')
        c = input('enter third number :: ')
        self.a=a
        self.b=b
        self.c=c
        print('a=',a)
        print('b=',b)
        print('c=',c)

y = B()
y.accept(2,3)
    

