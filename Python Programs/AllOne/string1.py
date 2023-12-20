# s='divya is a good boy'
# # string[start:stop:jump]
# print(s[::-1])  #reverse a string using slicing
# print("".join(reversed(s))) #Q- how is this?
# # del(s) #delete entire string even reference too
# # s = "moahn"
# l1 = list(s)
# # print(s)
# print(l1)
# l1[-3:]=['l','a','d','k','a']
# print(l1)
# print("".join(l1))

# print(s)

# string to list
s='divya prakash is a good boy'
list1 = s.split()
print(list1)
# list yo string
print(" ".join(list1))

# updating a single character
String3 = s[0:8] + 'p' + s[9:] 
print(String3) 

# deleting a single character
st = s[:8]+s[9:]
print(st)

# Printing hello in octal 
String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ") 
print(String1) 
  
# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ") 
print(String1) 
  
# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 
  
# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1) 