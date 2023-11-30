# tup=(1,'ram',43,2,53,5,3,5)
# print(len(tup))
# print(tup[0:len(tup)])
# print(tup.index(5,6,12))
# print(type(tup))

tup = (4,2,2,4,'ram','shyam','mohan')
try:
    user = int(input('Enter 0(super admin) and 1 (admin) :: '))
    if user==0:
        lst = list(tup)
        n  = int(input('how many numbers you want to add :: '))
        for i in range(n):
            lst.append(int(input('Enter you number :: ')))
        print(lst)
    elif user == 1:
        print('you can only access the data cannot do anything on it ')
        decide = input('Want to show all data y/ any key to exit?')
        if decide.lower() == 'y':
            print(tup[:])
        else:
            print('thanks for visiting')
    else:
        print('you have entered wrong')
except TypeError:
    print("type error got error")
except ValueError:
    print("value got erro")
except:
    print("kuch to garbar hai daya")
else:
    print("kuch exception nahi aya bhai")
finally:
    print('main to har hal me print ho jaunga')