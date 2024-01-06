class countobj:
    ctr=10
    def disp(self):
        print('Value of ctr = ',self.ctr)
    def accept(self):
        countobj.ctr = int(input('enter a number : '))
    
x=countobj()
x.disp()
y=countobj()
y.disp()
x.accept()
x.disp()
y.disp()