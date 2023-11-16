# Input: hello world 
# Output: HellO WorlD

def capFirstLastWord(s):
    l = s.split()
    res=[]
    for i in l:
       x= i[:1].upper()+i[1:-1]+i[-1:].upper()
       res.append(x)
    print(' '.join(res))

capFirstLastWord('every char is a string')