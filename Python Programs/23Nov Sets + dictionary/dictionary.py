# dic1 = {'key':'value'}
# print(dic1)
# print(type(dic1))

a = {2:['rays','hello'],3:'rays',3:'patna',4:'ara'}
# print(a)

# access value
# print(a[3])  
# print(a['3']) #if key not available, return KeyError

# print(a.get(2))  
# print(a.get(5))  #if key not available, return None

# a[2] = 'infosis'
print(a)

b = a.keys()
for i in b:
    print(i)
print(a.values())
