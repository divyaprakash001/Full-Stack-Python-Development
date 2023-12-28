class constest:
    a=0
    def __init__(self,a=20):
        print('parameterised constructor called')
        self.a=a
    def disp(self):
        print("value of a ::",self.a)
    
x = constest()
x.disp()
y = constest(23)
x.disp()
y.disp()