# def checkLetterDigit(s):
#     if s.isalnum():
#         print('alpha + digit ')
#     else:
#         print('sorry it is not alpha+digit')
    
# checkLetterDigit('divya99')
# checkLetterDigit('divya99divya')
# checkLetterDigit('divyadivya')

def checkLetterDigit2(s):
    flag_l = False
    flag_d = False
    for i in s:
        if i.isalpha():
            flag_l=True
        if i.isdigit():
            flag_d=True
    return flag_l and flag_d
    
print(checkLetterDigit2('divya99'))
print(checkLetterDigit2('divya99divya'))
print(checkLetterDigit2('divya'))