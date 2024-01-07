import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

print(type(y))  #dictionary type
# the result is a Python dictionary:
print(y["age"])