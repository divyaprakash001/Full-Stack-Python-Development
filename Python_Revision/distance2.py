class Distance:
    feet=inch=0
    
    def input(self,a,b):
        print('input called')
        Distance.feet = a  #or self.feet = a
        Distance.inch = b    #or Distance.inch = b
        # we can put self.inch in one variable and use them when need without self
    
    def disp(self):
        if self.inch>12:
            self.feet = self.feet + self.inch//12
            self.inch = self.inch % 12
        print(f'Feet :: {Distance.feet} \nInch :: {Distance.inch}')
        print(f'Feet :: {self.feet} \nInch :: {self.inch}')
    
d = Distance()
d.input(10,27)
d.disp()