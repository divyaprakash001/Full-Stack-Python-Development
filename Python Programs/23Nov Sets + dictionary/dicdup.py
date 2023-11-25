a = {3:'soft',5:'microsoft','pa':'siwan'}
print(a)
b=a
b = a.copy()  #to make copy or pure duplicate
b = dict(a)
if a is b:
    print('not duplicate')
else:
    print('duplicate')