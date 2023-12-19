class distance:
    feet=inch=0

    def disp(self):
        print('disp called')

    def check(self,a,b):
        if a>b:
            print('highest',a)
        else:
            print('highest',b)


# no need to pass argument
x = distance()  #internally  distance(0x21)
x.check(10,20)   #internally  check(0x21,10,20)
x.disp()         #internally  disp(0x21)