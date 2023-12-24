class Person:
    loaded = 'person loaded'

    
    def __init__(self,load,name,age,group):
        loaded = load
        self.name=name
        self.age=age
        self.group=group
        # print('static loaed ::',Person.loaded)
        print("constructor called")
    
    def disp(self):
        print('Name ::',self.name)
        print('Age ::',self.age)
        print('Group ::',self.group)
    
    @staticmethod
    def smethod(self):
        print('static method loaded first before constructor',Person.loaded)
    
p = Person('Divya loaded','Prakahs',24,'India')
Person.smethod(p)
p.disp()
