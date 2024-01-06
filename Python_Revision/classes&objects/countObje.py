class countObj:
    count=0
    def __init__(self):
        countObj.count = countObj.count + 1
        print('the number of object created',countObj.count)

for i in range(10):
    countObj()