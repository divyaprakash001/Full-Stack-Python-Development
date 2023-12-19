class distance:
    feet=inch=0

    def disp():
        print('disp called')

    def check(a,b):
        if a>b:
            print('highest',a)
        else:
            print('highest',b)


# no need to pass argument
x = distance
x.check(10,20)
x.disp()