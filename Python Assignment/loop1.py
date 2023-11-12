# 1. Wap in “Python‟ language to display “Python is General Purpose language” five times.

for i in range(5):
    print('Python is General Purpose language')

print('\n Ques. 2')
# 2. Wap in “Python‟ language to display “I like „Python‟ very much!” three times and each after two lines.
for i in range(3):
    print('I like \'Python\' very much!')
    print('\n\n')


# 3. Wap  in  “Python‟ language  to  display  “I  like  „Python‟  very  much!”  continuously  until  a  zero  is pressed



# 4. Wap in “Python‟ language to display the counting starting from 1 and up to 30.

for i in range(1,31):
    print(i)

# 5. 


# 6. Wap  in  “Python‟ language  to  accept  thirty  numbers  calculate  and  display  the  sum,  product and average value. 

sum=0
product=1
average=0

for i in range(30):
    num = int(input('Enter your number :: '))
    sum += num
    product *= num

print('The sum of the numbers :: ',sum)
print('The product of the numbers :: ',product)
print('The average of the numbers :: ',sum/30)


# 7. Wap in “Python‟ language to accept N numbers calculate and display the sum, product and average value

n = int(input('How many numbers you want to enter :: '))

sum=0
product=1
average=0

for i in range(n):
    num = int(input('Enter your number :: '))
    sum += num
    product *= num

print('The sum of the numbers :: ',sum)
print('The product of the numbers :: ',product)
print('The average of the numbers :: ',sum/n)


# 8. Wap in “Python‟ language to accept N numbers calculate and display the total count of even and odd numbers. 

n = int(input('How many numbers you want to enter :: '))
ecount=0
ocount=0

for i in range(n):
    num=int(input('Enter your number :: '))
    if num%2==0:
        ecount+=1
    else:
        ocount+=1

print('No of even :: ',ecount)
print('No of odds :: ',ocount)

# 9. Wap in “Python‟ language to accept N numbers calculate and display the total count of  +ve even and -ve odd numbers.

n = int(input('How many numbers you want to enter :: '))
pEvenCount=0
nOddCount=0

for i in range(n):
    num=int(input('Enter your number :: '))
    if num%2==0 and num > 0:
        pEvenCount+=1
    elif num%2 != 0 and num < 0:
        nOddCount+=1

print('No of positive even numbers :: ',pEvenCount)
print('No of negative odds numbers :: ',nOddCount)


# 10. Wap in “Python‟ language to accept N characters one-by-one calculate and display the total count of digits and alphabets.

n = int(input('How many characters you want to enter :: '))

alphaCount=0
digitCount=0

for i in range(n):
    ch = ord(input("Enter your character :: "))
    if ch >= 65 and ch <= 122:
        alphaCount+=1
    elif ch >= 48 and ch<=58:
        digitCount+=1
    else:
        print("other character")
print('Total number of digits',digitCount)
print('Total number of alphabets',alphaCount)


# 11. Wap in “Python‟ language to accept N numbers check and display the smallest and largest value. 

n = int(input('How many numbers you want to enter :: '))







# 12. Wap in “Python‟ language to accept a number calculates and display the total count of digits. 
 
n = int(input('How many numbers you want to enter :: '))
dcount=0





# 13. Wap  in  “Python‟  language  to  accept  a  number  calculates  and  display  the  sum,  product  and 
# average of the digits. 
 
n = int(input('Enter your number :: '))
dlen = len(str(n))
sum=0
product=1
average=0

while n>0:
    d=n%10
    sum+=d
    product*=d
    n=n//10
print('The sum of the digits of given number ',sum)
print('The product of the digits of given number ',product)
print('The average of the digits of given number ',sum/dlen)





# 14. Wap in “Python‟ language to generate even series from 1 to  50. 

for i in range(2,51,2):
    print(i,end=' ')


print()
# 15. Wap in “Python‟ language to generate odd series from 1 to 50. 

for i in range(1,51,2):
    print(i,end=' ')


# 16. Wap in “Python‟ language to accept a number, display it in reverse order 

n = int(input('Enter your number :: '))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print('The reverse of the given number is ',rev)



# 17. Wap in “Python‟ language to generate a table of any number. 

tabNum = int(input('Table of which number you want :: '))
n=10

for i in range(1,n+1):
    print(tabNum,'X',i,'=',tabNum*i)


# 18. Wap in “Python‟ language to accept a number, check and display whether the number is prime or not. 

n = int(input('Enter your number to check prime or not :: '))
flag=False
for d in range(2,n//2+1):
    if n%d==0:
        flag=True
        break

if n==1:
    print("Not a prime number")
elif flag:
    print('not a prime number')
else:
    print("prime number")





# 19. Wap in “Python‟ language to accept initial and final position and find the  prime numbers between the 
# initial and final position. 

strt = int(input('Enter your initial position :: '))
fnl = int(input('Enter your final position :: '))








# 20. Wap in “Python‟ language to accept a number, check and display message whether it perfect number 
# or  not. 

n = int(input('Enter your number :: '))
sum=0
for d in range(1,n//2+1):
    if n%d==0:
        sum+=d

if sum==n:
    print('The given number {} is a perfect number'.format(n))
else:
    print('The given number {} is not a perfect number'.format(n))





# 21. Wap in “Python‟ language to accept a number, check and display whether the  number is Armstrong 
# or  not. 

n = int(input('Enter your number :: '))
num=n
l=len(str(n))
arm=0

while n>0:
    d=n%10
    arm+=d**l
    n=n//10

if arm==num:
    print("The given number {} is an armstrong number".format(num))
else:
    print("The given number {} is not an armstrong number".format(num))




# 22. Wap in “Python‟ language to accept initial and final position, print Armstrong number between initial and final position. 

strt = int(input('Enter your initial position :: '))
last = int(input('Enter your final position :: '))
l=len(str(n))
armCount=0

while n>0:
    d=n%10
    arm+=d**l
    n=n//10




# 23. Wap in “Python‟ language to accept a number and display its factorial value. 
 
num = int(input('Enter your number to get factorial :: '))
factorial=1

for i in range(1,num+1):
    factorial*=i
print('Factorial of',num,'::',factorial)



# 28. Wap in “Python‟ language to accept two numbers check and display the Highest Common Factor or Greatest Common Factor 

x = int(input('Enter your first number :: '))
xn=x
y = int(input('Enter your second number :: '))
yn=y

while y != 0:
    (x, y) = (y, x % y)

print('The greatest common factor of',xn,'and',yn,'is',x)


# 29. Wap in “Python‟ language to accept two numbers check and display the Lowest Common Factor . 

x = int(input('Enter your first number :: '))
xn=x
y = int(input('Enter your second number :: '))
yn=y
lcm=0

if x>y:
    z=x
else:
    z=y

while True:
    if z%x==0 and z%y==0:
        lcm=z
        break
    z+=1
print('The lowest common factor of',xn,'and',yn,'is',lcm)



# 30. Wap in “Python‟ language to display 20 terms of Fibonacci series . (i.e 0,1,1,2,3, . ). 

a=0;b=1
n = 20
print('Fibonacci series ',a,b,end=' ')
for t in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=' ')


 
# 31. Wap in “Python‟ language to accept  a positive integer value, determine and print its binary 
# equivalent. 
n = int(input('Enter your number :: '))
nbin = bin(n)
print(nbin)


 
# 32. Wap in “Python‟ language to accept a positive value, convert into hexadecimal equivalent. 
n = int(input('Enter your number :: '))
hexn = hex(n)
print(hexn)


# 33. Wap in “Python‟ language to display the total count of Leap Years between 1000 and 2009

ycount = 0
strt=1000
last=2009

for year in range(strt,last+1):
    if year % 400 == 0 and year % 100 == 0:
        ycount+=1
    elif year % 4 ==0 and year % 100 != 0:
        ycount+=1

print('No of leap years between {} and {} is {}'.format(strt,last,ycount))

# 34. 


# 35. Wap in “Python‟ language to calculate and display the Fibonacci series up to n terms
a=0;b=1
n = int(input('Enter your number :: '))
print('Fibonacci series ',a,b,end=' ')
for t in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=' ')

# 36.a
for i in range(5):
    for j in range(i+1):
        print(j+1,end='')
    print()

print()
# 36.b
# for i in range(5):
#     for j in range(4,i,-1):
#         print(end='  ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# 36.c
for i in range(5):
    for j in range(5,i,-1):
        print(1,end='')
    print()

print()
# 36.d
for i in range(5):
    for j in range(i+1):
        print(5,end='')
    print()

print()
# # 36.e
# for i in range(5):
#     for j in range(4,i,-1):
#         print(end=' ')
#     for j in range(5):
#         print(j,end=' ')
#     for j in range(5,-1):
#         print(j,end=' ')
#     for j in range(5):
#         print(j,end=' ')
#     print()

# 36.f
# 36.g




# 36.h=>  
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

print()
# 36.i=>  
for i in range(5):
    for j in range(4,i,-1):
        print(end='  ')
    for j in range(i+1):
        print('*',end=' ')
    print()

print()
# 36.j=> 

for i in range(1,6):
    for j in range(4,i-1,-1):
        print(end='  ')
    for j in range(1,2*i):
        print('*',end=' ')
    print()

print()
# 36.k=> 

for i in range(5):
    for j in range(i+1):
        if(i+j)%2==0:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()