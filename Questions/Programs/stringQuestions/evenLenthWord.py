# 1st way to print the even length word

def evenLenWord(s):
    l1 = []
    for i in range(len(s.split())):
        if len(s.split()[i])%2==0:
            l1.append(s.split()[i])
    st = ' '.join(l1)
    print(st)        

evenLenWord('i am a good programmer and will be the best.')

# 2nd way
def evenLenWord(n):
    s=n.split() 
    for i in s: 
        if len(i)%2==0: 
            print(i,end= ' ')

evenLenWord("I am a good programmer and will be the best.")