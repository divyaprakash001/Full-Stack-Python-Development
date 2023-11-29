class Math:
    @staticmethod
    def add(a,b):
        return a+b
    
# In static method , there is not need to create any instance of the class
print(Math.add(10,20))