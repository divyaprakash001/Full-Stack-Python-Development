class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def makeSound(self):
        print("Sound made by animal")
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species='Dog')
        self.breed = breed
    
    def makeSound(self):
        print("Barking")

d= Dog('Jacky','indi')
print(d.name)
print(d.breed)
print(d.species)
d.makeSound()


a= Animal('Cow','indus')
print(a.name)
print(a.species)
a.makeSound()