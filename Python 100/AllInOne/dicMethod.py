ep1 = {122:45, 123:89, 567:69, 670:69}
ep2={222:67,566:90}

ep1.update(ep2)
# ep1.clear() #clear the dict.. means empty dict...
# ep1.pop(122) #remove desired key with value
ep1.popitem() #remove last key-value pair
# del ep2 #delete the dic... with reference if not giving specific key
# print(ep2)
del ep1[122]  #only delete the specific key with value
print(ep1)
