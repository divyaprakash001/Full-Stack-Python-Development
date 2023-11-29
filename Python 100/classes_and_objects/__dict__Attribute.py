class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
p = Person('ahrry',23)
print(p.__dict__)
