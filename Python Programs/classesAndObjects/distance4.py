class Distance:
    feet=inch=0

    def calculate(self):
        # feet = self.feet  #we can do this to prevent use of self each time
        # inch = self.inch
        if self.inch > 12:
            self.feet = self.feet + self.inch//12
            self.inch = self.inch%12
    
    def disp(self):
        print('Feet : ',self.feet,'Inch : ',self.inch)

    def input(self,feet,inch):
        Distance.feet = feet
        self.inch = inch
    
x  = Distance()
x.input(13,18)
x.calculate()
x.disp()

x.input(14, 8)
x.calculate()
x.disp()   