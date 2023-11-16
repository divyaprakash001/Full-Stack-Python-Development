import math

# without math.ceil()
def checkSymmetric(s):
    if len(s)%2==0:
        middle = int(len(s)/2)
    else:
        middle = int(len(s)/2)+1
    first_half = s[:middle]
    second_half= s[middle:]
    if first_half == second_half:
        print('The given is symmetric')
    else:
        print('The given is non symmetric')

checkSymmetric('amaama')
checkSymmetric('daldal')
checkSymmetric('dalda')

print('===========================')
# with math.ceil()
def checkSymmetric(s):
    middle = math.ceil(len(s)/2)
    first_half = s[:middle]
    second_half= s[middle:]
    if first_half == second_half:
        print('The given is symmetric')
    else:
        print('The given is non symmetric')

checkSymmetric('amaama')
checkSymmetric('daldal')
checkSymmetric('dalda')
