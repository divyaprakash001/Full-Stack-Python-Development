class Person:
    name='Rohit'
    age=24
    occupation = "developer"

    def info(self):
        print(f"{self.name}\'s age is {self.age} ")

a = Person()
print(a)
print(a.name)
print(a.age)
print(a.occupation)
a.info()