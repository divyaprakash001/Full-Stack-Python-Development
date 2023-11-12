a='  Rays   '
print(a,len(a),sep=',')
print(type(a))

a=a.lstrip() #remove whitespace on left side if no any characters available
print(a,len(a),sep=',')
a=a.rstrip() #remove whitespace on right side if no any characters available
print(a,len(a),sep=',')

a='  Rays   '
print(a,len(a),sep=',')
a=a.strip() #remove whitespace on both side if no any characters available
print(a,len(a),sep=',')

b='rAys EdUtECh pVt lTD.'
print(b)
print(b.capitalize())
print(b.lower())
print(b.upper())
print(b.center(len(b)+8,'$'))
print(b.count('t'))

print(b.find('t',9,20))  # Return the lowest index in S where substring sub is found,

print("-----------------------------------")
c='Rays edutech pvt ltd'
print(c.count('b'))
print(c.find('b'))  #if not found return -1
print(c.index('pvt')) #if not found return ValueError

print(c.endswith('ltd'))

'''sen = input("Enter your profile summary ")

if sen.lower().find('python') != -1 :
    print("your resume is selected")
else:
    print("sorry your resume is not selected.")

tcount = sen.lower().count('python')

if tcount > 0 :
    print("You are selected as you have used python ,"+ str(tcount) + " times")
else:
    print("You are not selected as you have used python ,"+ str(tcount) + " times")

senb = input("Enter a valid full sentence :: ")
if senb.endswith('.')==True:
    print("Yeah ! You have written a full sentence.")
else:
    print("Sorry! You haven't write a full sentence")'''

a=''' This is multiline string
that i want to use it and test whether the given line in gfg is true or not '''
print(a)

# reversing a string using slicing
gfg="Rama"
print(gfg[::-1])

# reversing a string using join and reversed method
print("".join(reversed(gfg)))