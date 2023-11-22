def func1():
    try:
        l = [1,2,3,4,5]
        i  = int(input('Enter your index :: '))
        return 1
    except:
        print('i am in exception')
        return 0
    print('i am tryng to execute')

x = func1()
print(x)