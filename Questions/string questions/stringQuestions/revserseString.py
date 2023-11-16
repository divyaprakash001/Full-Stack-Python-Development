# 1st way
def reverseString(s):
    print(s[::-1])

reverseString('divya prakash')

# 2nd way
def reverseString2(s):
    print(''.join(reversed(s)))

reverseString2('jay prakash')

# 3rd way
def reverseString3(s):
    rev = ''
    for c in s:
        rev = c+rev
    print(rev)

reverseString3('chandra prakash')