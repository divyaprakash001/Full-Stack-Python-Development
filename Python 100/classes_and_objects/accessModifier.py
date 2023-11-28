# private access modifier has no strict rule

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    def __showDetails(self):
        print(f'The name is {self.__name}')
        print(f'The age is {self.__age}')

    def dikhaDoBhai(self):
        self.__showDetails()


p= Person('harry',24)
# print(p.__name) #cannot be accessed => AttributeError:
print(p._Person__name) #can be accessed by using this
p.dikhaDoBhai()