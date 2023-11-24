# x = 10

def my_function():
    global x
    x=5
    y=20
    print('y =',y)

my_function()
print('using global keyword, global variable x =',x)
# print(y)