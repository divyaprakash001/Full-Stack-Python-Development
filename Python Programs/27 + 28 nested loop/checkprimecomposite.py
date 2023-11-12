n=int(input("Enter your number :: "))
flag=False

for t in range(2,n//2+1):
    if n%t==0:
        flag=True
        break

if n==1:
    print("neithr prime nor composite")
elif flag:
    print("composite number")
else:
    print("prime number")
