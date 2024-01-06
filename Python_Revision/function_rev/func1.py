def func1(*args):
    print('hello',args)
    print(type(args))
    return args
# func1(1,2,3,4,5,6,'he','be')
f = func1(1,2,3,4,'he','be','te')
print(f[0],f[1])

def parent(child1,child2,child3):
    print('the yougest is',child2)

parent(child1='rohan',child2='sohan',child3='mohan')

# arbitrary keyword
def myfunc(**kids):
    print("his last name is",kids["lname"])

myfunc(fname="rohan",lname="kumar")

def passlist(food):
    for item in food:
        print(item)

passlist(['orange','papaya','guava','grapes','apple'])

# only positional arguments
def mydef(x,/):
    print("the value of x is",x)

mydef(3)

# positional
def mydef2(x):
    print("the value of x is",x)

mydef2(x=13)

# only keyword argument
def mydef2(*,xx):
    print("the value of xx is",xx)

mydef2(xx=43)


def my_function(a, b, /, *, c, d):
  print('the total is',a + b + c + d)

my_function(5, 6, c = 7, d = 8)

def tri_recursion(k):
  '''this is recursion function'''
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print(tri_recursion.__doc__)