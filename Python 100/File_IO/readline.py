f = open('E:\Python Full Stack Development\Python 100\File_IO\marks.txt','r')
i=0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f'Marks of student {i} in Math is {m1}')
    print(f'Marks of student {i} in Math is {m2}')
    print(f'Marks of student {i} in Math is {m3}')
    print(line)