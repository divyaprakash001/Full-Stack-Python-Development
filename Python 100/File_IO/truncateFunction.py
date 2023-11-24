with open('E:\\Python Full Stack Development\\Python 100\\File_IO\\file.txt','w') as f:
    f.write('Hello World')
    f.truncate(5)

with open('E:\\Python Full Stack Development\\Python 100\\File_IO\\file.txt','r') as f:
    print(f.read())
