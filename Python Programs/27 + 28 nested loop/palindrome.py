''' Accept a value from the keyboard, check and display a message whether given value is palindrome or not '''

a=input("Enter a value:: ")
b=''

for c in a:
    b=c+b

if a==b:
    print("palindrome")
else:
    print("not palindrome")