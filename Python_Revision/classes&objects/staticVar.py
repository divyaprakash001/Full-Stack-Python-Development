class staticVar:
    a=10  #static variable or class level variable

    def disp(self):
        # print("value of a=",a)
        print("value of a =",staticVar.a)
        # self.a = 100  #this make instance variable accessed through object reference
        staticVar.a=120
        print('value a : ',self.a)

    

print(staticVar.a)
x = staticVar()
x.disp()
print("val of a :: ",x.a)
print("val of a from outside :: ",staticVar.a)