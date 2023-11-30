dic = {
    'name':'Harry',
    'age':24,
    56:'cow'
}
print(dic[56])
print(dic.get('name'))
print(dic.keys())
print(dic.values())
print(dic.items())
print(type(dic.items()))

for key in dic.items():
    print(type(key))