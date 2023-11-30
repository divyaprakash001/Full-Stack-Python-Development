l = [2,4,5,7,9,5,2,8]
def filter_function(a):
    return a>4

newl = filter(filter_function,l)
print(list(newl))

newnewl = filter(lambda a : a>4,l)
print(list(newnewl))