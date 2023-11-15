n=int(input("how many no\' u want ? "))
ecount=0
ocount=0
while n>0:
    num=int(input("Enter your number :: "))
    if num%2==0:
        ecount+=1
    else:
        ocount+=1
    n=n-1
print("even number :: ",ecount)
print("odd number :: ",ocount)

    