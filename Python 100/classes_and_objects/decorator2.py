def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function.")
    return mfx


@greet
def hello():
    print('hello world')

# hello()

# @greet()
def add(a,b):
    print(a+b)

greet(add)(1,2)