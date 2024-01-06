class Person:
    loader= 'loaded'            #static variable or class level variable
    def method(self,a):
        '''This is method documentation'''
        self.name='mohit'        #non-static variable or instance variable
        print("method called")
        age=a                    #age is method scope variable or local variable
        print(f'age is {age}')
        print("value of loader",self.loader)
        print("value of loader",Person.loader)

  

print(Person.loader)            #static variable before object creation through class name only
p = Person()                    #keeping address of Person to p
print(p.loader)                 #static variable after object creation through object reference
print(Person.loader)            #static variable after object creation through class name
# print(Person.name)            #cannot accessed instance variable with class name or before objetc creation
# print(p.name)
# p.name='rohit'                  #re-assign the value of instance variable name
# print(p.name)
p.method(25)
# print(dir(p))
# print(p.__dict__)
# print(help(p.method))


                                # del q  #i think it deallocate the class reference
                                # print(q.method(23))

                                # all object of same clas access the same location static variable
                                # instance variable allocates separately for all object of same class
                                # method scope variable allocated when function is calling and available till method execution