# a=[1,2,43]
# b=[1,2,43]

# print(a is b)  #False
# print(a == b) #True

a=(1,2,3)
b=(1,2,3)

print(a is b)  #True
print(a == b)  #True

a = "Harry"
b = "Harry"

print(a is b)  #True
print(a == b)  #True

a=None
b=None
print(a is b)  #True
print(a is None)  #True
print(a == b)  #True
