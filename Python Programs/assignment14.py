def calculate_all_in_one(basic):
    da,hra,ta,cca,gross=0,0,0,0,0
    if basic > 25000:
        da = basic * 0.4
    else:
        da= basic * 0.3
    
    hra = basic * 0.4
    
    if basic < 12000:
        ta = 800
        cca = 300
    else:
        ta = 1000
        cca = 500
    gross = basic + da+hra+ta+cca
    return da,hra,ta,cca,gross
    
basic = 0

def printDetails():
    print('SNO',sno)
    print('CODE',code)
    print('NAME',name)
    print('CATEGORY',category)
    print('BASIC',basic)
    print('DA',data[0])
    print('HRA',data[1])
    print('TA',data[2])
    print('CCA',data[3])
    print('GROSS',data[4])

    


for i in range(2):
    sno = int(input('Enter sno :: '))
    code = input('Enter code number :: ')
    name = input('Enter name of the employee :: ')
    category = input('Enter category of the employee:: ')
    basic = int(input('Enter basic salary of the employee :: '))
    data = calculate_all_in_one(basic)
    printDetails()
    
    
