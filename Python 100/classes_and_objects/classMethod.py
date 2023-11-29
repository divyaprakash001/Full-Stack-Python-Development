class Employee:
    company = "Apple"
    
    def show(self):
        print(f'The name is {self.name} and the company name is {self.company}')
    
    @classmethod
    def changeCompany(cls,newCompany):
        cls.company = newCompany
    
e1 = Employee()
e1.name='Harry'
e1.show()
print(Employee.company)
e1.changeCompany('tesla')
print(Employee.company)
e1.show()