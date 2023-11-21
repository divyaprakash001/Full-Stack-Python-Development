''' Accept N numberd from keyboard and display it's elements in LIFO fashion '''

n = int(input('Enter your number :: '))
v = []
for i in range(n):
    v.append(int(input('Enter a number :: ')))
print(v)

while len(v)>0:
    print(v.pop())