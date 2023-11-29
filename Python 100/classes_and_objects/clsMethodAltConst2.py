class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def from_string(cls,string):
        name,age = string.split(',')
        return cls(name,int(age))
    
p = Person.from_string("john doe,30")
print(p.name)
print(p.age)