class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showDetails(self):
        print(f"The name of the employee :: {self.name}")
        print(f"The id of the employee :: {self.id}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e1 = Employee('Harry',120)
e1.showDetails()
print("----------------")
e2 = Programmer('Rohan',410)
e2.showDetails()
e2.showLanguage()

    
