a = {'apple','orange','mango','apple',23,'banana','sfsg'}
# print(a,type(a))
# accessing element of sets
# print(a[0])  #cannot do indexing as not it is unordered
# print(a[1:4])  #cannot do slicing

# value change
# a[0]=20 # cannot do like this

b = a.add('rama')
# print(a)
# print(b)  # None

# adding multiple values
# b = a.update((3,4,'shyama'))
# print(a)
# print(b)

# deleting an item
# # a.clear()
print('============')
# a.remove('rana')  #if not available  raise KeyError
# print(a)

# b = a.discard('sona')  # no error if not available
# print(a)
# print(b)  #None

# b = a.pop()
# print(b)

a  = {} # empty dictionary not an empty set

a = set() #empty set
print(type(a))