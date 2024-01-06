class Inheri:
    def __init__(self):
        print("this is a constructor of parent class")
    def firstmethod(self):
        print("this is the first method of the parent class")
    def secondmethod(self):
        print('this is the second method of the parent class')

class child(Inheri):
    def __init__(self):
        print("this is a constructor of child class")
    def firstmethod(self):
        print("this is the first method of the child class")
    def secondmethod(self):
        print("this is the second method of the child class")

x = child()
x.firstmethod()
x.secondmethod()