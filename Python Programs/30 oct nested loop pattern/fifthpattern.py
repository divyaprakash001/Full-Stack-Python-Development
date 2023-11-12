'''
     A
    BAB
   CBABC
  DCBABCD
 EDCBABCDE
'''

i=0
while i<5:
    j=4
    while j>i:
        print(end=' ')
        j=j-1
    j=65+i
    while j>64:
        print(chr(j),end='')
        j=j-1
    j=66
    while j<66+i:
        print(chr(j),end='')
        j=j+1
    print()
    i=i+1

print("usinf for loop")

for i in range(5):
    for j in range(4,i,-1):
        print(end=' ')
    for j in range(65+i,64,-1):
        print(chr(j),end='')
    for j in range(66,66+i):
        print(chr(j),end='')
    print()

