try:
    raise NameError('Hi there!')
except NameError as n:
    print(f"the error is {n}")
    # raise