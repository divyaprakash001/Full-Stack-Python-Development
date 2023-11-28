class Person:
    def __init__(self,value):
        self._value=value

    @property
    def tenx_value(self):
        return 10 * self._value
    
    @tenx_value.setter
    def tenx_value(self,new_value):
        self._value = new_value/10
    
    def show(self):
        print(f'The value is {self._value}')

p = Person(10)
p.tenx_value = 67  #setting the value
print(p.tenx_value)
print(p._value)
