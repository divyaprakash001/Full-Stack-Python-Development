#1st way
def findLength(s):
    print(len(s))

findLength('string')

# 2nd way
def lengthOfString(s):
    lenCount=0
    for i in s:
        lenCount+= 1
    print(lenCount)

lengthOfString('string')

# 3rd way
def lenString(s):
    lencount=0
    while s[lencount:]:
        lencount+=1
    print(lencount)

lenString('string')

# count len without space
def countLenAvoidSpace(s):
    lencount=0
    for i in s:
        if i.isspace():
            s = s.replace(' ','')
    print(len(s))

countLenAvoidSpace('ram is boy')


# count len without space 2nd way
def countLenAvoidSpace(s):
    lencount=0
    s = s.replace(' ','')
    for i in s:
        lencount+=1
    print(lencount)

countLenAvoidSpace('ram is boy')