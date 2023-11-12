'''
0
1 0
0 1 0
1 0 1 0
0 1 0 1 0
'''
i=0
while i<5:
    j=0
    while j<i+1:
        if (i+j)%2==0:
            print(0,end=' ')
        else:
            print(1,end=' ')
        j=j+1
    print()
    i=i+1

print("using for loop")

for i in range(5):
    for j in range(i+1):
        if (i+j)%2==0:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()