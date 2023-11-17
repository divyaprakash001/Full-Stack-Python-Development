countries1=list(('India','Australia',2))
countries2=['New Zealand','England',3]
# print(countries1)
# print(countries2)

countries1.pop(2)
print(countries1)
del countries2[2] # instead of pop() we can use del
print(countries2)