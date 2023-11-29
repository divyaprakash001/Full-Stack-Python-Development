class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @classmethod
    def from_str(cls,string):
        return cls(string.split('-')[0],int(string.split('-')[1]))
    


e1 = Employee('harry',120000)
print(e1.name)
print(e1.salary)

string= 'john-10000'

e2 = Employee(string.split('-')[0],string.split('-')[1])
print(e2.name)
print(e2.salary)


string= 'robert-11000'
e3 = Employee.from_str(string)
print(e3.name)
print(e3.salary)


