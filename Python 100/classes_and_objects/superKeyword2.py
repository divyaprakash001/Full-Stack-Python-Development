class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
    
e = Employee('harry','420')
print(e.name)
p = Programmer('rohan','639','PYTHON')
print(p.name)
print(p.id)
print(p.lang)
