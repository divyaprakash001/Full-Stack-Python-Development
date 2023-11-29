class Employee:
    companyName="Apple"
    noOfEmployee = 0

    def __init__(self,name):
        self.name=name
        self.raiseAmount=0.02
        Employee.noOfEmployee += 1
    
    def showDetails(self):
        print(f'The employee no {Employee.noOfEmployee} name is {self.name} in the company {Employee.companyName} raise the amount of {self.raiseAmount}')

# Employee.showDetails(emp2)
# Employee.showDetails(emp1)

emp1 = Employee('harry')
emp1.raiseAmount=0.03
emp1.showDetails()
# emp1.companyName="google"
Employee.companyName="Nestle"
print(emp1.companyName)
emp2 = Employee('rohan')
emp2.showDetails()
print(emp2.companyName)