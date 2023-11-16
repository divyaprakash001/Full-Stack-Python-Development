def removeCharacter(s,index):
    l=[]
    for i in s:
        l += i
    for i in range(len(l)+1):
        if l[i]==l[index]:
            l.pop(i)
            break
    s = str(l)
    print(s)

removeCharacter('ramayan',4) #remove the character at desired index of a string