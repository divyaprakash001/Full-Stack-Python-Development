# i=0
# while i<5:
#     j=4
#     while j<i:
#         print(end=' ')
#         j=j-1
#     j=0
#     while j<=i:
#         print("*",end=' ')
#         j=j+1
#     print()
#     i=i+1

for i in range(5):
    for j in range(4,i,-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()