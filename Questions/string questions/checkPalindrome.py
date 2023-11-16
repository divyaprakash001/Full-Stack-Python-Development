# applicable only for string data type
def checkPalindrome(s):
    rev = s[::-1]  
    if rev==s:
        print("palindrome")
    else:
        print("not a palindrome")

checkPalindrome('dalad')


# universal as for string and int type but as a string input also
def checkUniversalPalindrome(s):
    if type(s) == int:
        s = str(s)
    b=''
    for c in s:
        b = c+b
    if b == s:
        print('palindrome')
    else:
        print('not a palindrome')

checkUniversalPalindrome(121)
checkUniversalPalindrome('ama')




