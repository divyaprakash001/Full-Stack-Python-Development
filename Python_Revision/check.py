# exceptional case
class checker:
    def disp():
        print("disp called")
    
    def check(a,b):
        if a>b:
            print("highest",a)
        else:
            print("highest",b)
        
x = checker
x.disp()
x.check(12,7)