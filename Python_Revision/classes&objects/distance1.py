class Distance:
    feet=inch=0
    def input(self,a,b):
        print('input called')
        Distance.feet = a  #or self.feet = a
        self.inch=b    #or Distance.inch = b
    
    def disp(self):
        print('feet',Distance.feet,'\nInch',self.inch)
        print(f'Feet :: {Distance.feet} \nInch :: {self.inch}')
    
d = Distance()
d.input(10,24)
d.disp()