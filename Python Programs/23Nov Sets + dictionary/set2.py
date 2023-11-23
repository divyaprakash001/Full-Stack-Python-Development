x = {'a','b','c','d'}
y = {'b','c','e'}
# r = (x.union(y))
# print(x)
# print(y)
# print(r)

# print('--------------')
# p= x.intersection(y)
# t = x.difference(y)
# print(p)
# print(x)
# print(y)
# print(t)


# r = x.symmetric_difference(y)
# r = x.symmetric_difference_update(y)  #return type None
m = x  #copy reference only
p=x.copy()  #duplicate
print(p)
x.add('dhdd')
print(x)
print(m)
print(y)
# print(r)

print('--------------')

if m is x :
    print('duplicate')
else:
    print('not duplicate')

if p is x :
    print('duplicate')
else:
    print('not duplicate')