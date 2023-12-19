class distance:
    feet=inch=0
    def input(self,a,b):
        distance.feet=a
        self.inch = b
    def disp(self):
        print('feet=',distance.feet,'inch=',self.inch)
    
x = distance()
x.input(10,20)
x.disp()

# print(id(x))