''' Accept a number from keyboard, check and display whether given number is armstrong or not '''
# if sum of power(according to the no of digts) of its digit is equal to the given number is called armstrong number


n=int(input("Enter any number :: "))
num=n
l=len(str(n))
arm=0
while n>0:
    d=n%10
    # arm+= d**l
    arm += pow(d,l)
    n=n//10

print(num)
print(arm)

if arm==num:
    print("Armstrong")
else:
    print("Not Armstrong")