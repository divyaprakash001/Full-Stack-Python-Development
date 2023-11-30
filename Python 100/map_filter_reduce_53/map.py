def cube(x):
    return x*x*x

l = [1,2,4,6,4,3]
newl = []

for item in l:
    newl.append(cube(item))

print(newl)
print('------------------')
newlm = list(map(cube,l))
print(newlm)

numbers=[1,2,3,4,5,6]
squared = map(lambda x: x*x,numbers)
print(list(squared))