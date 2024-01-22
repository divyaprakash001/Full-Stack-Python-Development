'''
    Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

def odd():
    max = int(input('Enter your max number to list out odd numbers '))
    oddlist=[]
    for i in range(1,max):
        if i % 2 != 0:
            oddlist.append(i)
    print(oddlist)

odd()

'''
max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)
'''