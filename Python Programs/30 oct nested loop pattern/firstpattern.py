i=0
while i<5:
    j=0
    while j<=i:
        print("*",end=' ')
        j+=1
    print()
    i+=1

print("\n")
print("using for loop\n")

for i in range(5):
    for j in range(i+1):
        print("*",end=' ')
    print()