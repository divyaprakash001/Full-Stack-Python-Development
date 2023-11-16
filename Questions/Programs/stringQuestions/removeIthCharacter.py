def removeCharacter(s,index):
    l=[]
    for i in s:
        l += i
    for i in range(len(l)+1):
        if len(l)>index:
            if l[i]==l[index]:
                l.pop(i)
                break
        else:
            print('sorry, no index found')
            break
    s = "".join(l)
    print(s)

removeCharacter('ram',3) #remove the character at desired index of a string

# using replace method , remove first occurence only
def removeChar(s,ch):
    s = s.replace(ch,'',1)
    print(s)

removeChar('ramayana','a')