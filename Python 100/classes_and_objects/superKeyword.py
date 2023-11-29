class ParentClass:
    def parentMethod(self):
        print('This is the parent method')


class ChildClass(ParentClass):
    def parentMethod(self):
        print('This is the parent method of child class')

    def childMethod(self):
        print('This is the child method')
        super().parentMethod()
    
c = ChildClass()
c.childMethod()
c.parentMethod()
    