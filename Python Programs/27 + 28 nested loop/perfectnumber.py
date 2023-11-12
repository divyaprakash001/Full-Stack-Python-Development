# accept a number from keyboard, check and dosplay whther the given number is a perfect number or not
# logic for perfect number:- if the sum of its divisor is equal to the given number ==> perfect number

n = int(input("Enter any number :: "))
sum=0
for d in range(1,n//2+1):
    if n%d==0:
        sum+=d

if sum==n:
    print("perfect ")
else:
    print("not perfect")

print(sum)
