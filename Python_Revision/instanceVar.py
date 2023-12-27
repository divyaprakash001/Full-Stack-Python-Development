class instanceVar:
    staVar = 'static'
    def __init__(self):
        self.a=10
        self.b=20

    # def start(self):
    #     self.a=10
    #     self.b=20

    def disp(self):
        self.a = 40
        print('The value of a is',self.a)
        print('The value of b is',self.b)
    
x = instanceVar()
# x.start()
x.disp()
x.a=30   #we can re-assign the instance var
print(x.a)  #access by object reference 
instanceVar.staVar = 'staticVar'  #we can re-assign the static var 
print(x.staVar)  #we can access the static var using object reference
del instanceVar  #delete the object
print(instanceVar.staVar)  #we can access the static var using class name