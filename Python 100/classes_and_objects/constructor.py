# class Person:
#     def __init__(self):
#         print('Hey! I am a constructor')

#     def info(self):
#         print(f"{self.name} is a {self.occu}")
    
# a = Person()
# b = Person()

class Person():
    def __init__(self,name,occu):
        print('Hey i am a person')
        self.name=name
        self.occu = occu
    def info(self):
        print(f"{self.name} is a {self.occu}")

a = Person('Harry','developer')
b = Person('Divya','HR')

a.info()
b.info()
