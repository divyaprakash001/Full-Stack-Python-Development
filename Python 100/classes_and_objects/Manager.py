from inheritance import Programmer,Employee

class Manager(Programmer,Employee):

    def showPower(self):
        print(f'Manager is the upstream of programmemr and employee. {self.showLanguage}')

print("----------------------")
m = Manager('rohit',123)
print("----------------------")
m.showDetails()
print("----------------------")
m.showLanguage()
print("----------------------")
m.showPower()
print("----------------------")
