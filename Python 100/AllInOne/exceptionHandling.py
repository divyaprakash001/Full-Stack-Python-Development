a = input('Enter your number :: ')
print(f'The multiplication table of {a} is ')
try:
    for i in range(1,11):
        print(f'{int(a)} x {i} = {int(a)*i}')
except ValueError as v:
    print(v,'value')
except NameError as n:
    print(n,'name')
except Exception as e:
    print(e,'eee')
except Exception as f:
    print(f,'last')
else:
    print('sab kuch thik rha bhai main ese block se bol rha hu')
finally:
    print('main finally block se bol rha hu bhai ye to bilkul print hoga bhai g')