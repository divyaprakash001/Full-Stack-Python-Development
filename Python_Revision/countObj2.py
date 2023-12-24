class countobj:
    ctr=0
    def disp(self):
        print('object created',countobj.ctr,'times')
        countobj.ctr=countobj.ctr+1
    
    
for i in range(3):
    countobj().disp()   #anonymous object