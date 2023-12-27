class Inheri1:
    def __init__(self):
        print("this is a constructor of parent1 class")
    def firstmethod(self):
        print("this is the first method of the parent1 class")
    def secondmethod(self):
        print('this is the second method of the parent1 class')

class Inheri2:
    def __init__(self):
        print("this is a constructor of parent2 class")
    def firstmethod(self):
        print("this is the first method of the parent2 class")
    def secondmethod(self):
        print('this is the second method of the parent2 class')

class child(Inheri2,Inheri1):
    def __init__(self):
        print("this is a constructor of child class")
    # def firstmethod(self):
    #     print("this is the first method of the child class")
    # def secondmethod(self):
    #     print("this is the second method of the child class")

x = child()
x.firstmethod()
x.secondmethod()