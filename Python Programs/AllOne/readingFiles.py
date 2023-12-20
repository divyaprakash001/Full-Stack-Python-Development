coun_file =  open('Python Extra Learning\\countries.txt','r')
# print(coun_file.readlines()[3])
# print(coun_file.readlines())

for lines in coun_file.readlines():
    print(lines,end='')

coun_file.close()