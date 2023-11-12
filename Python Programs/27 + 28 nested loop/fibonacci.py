a=0;b=1
n=10
print("The fibonacci series ",a,b,end=' ')
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=' ')