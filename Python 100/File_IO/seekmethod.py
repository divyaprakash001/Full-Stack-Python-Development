with open('E:\\Python Full Stack Development\\Python 100\\File_IO\\file.txt','r') as f:
    print(type(f))
    # move to 10th bytes in the file
    f.seek(6)
    # saved the current position
    print(f.tell())
    # read the next 5 bytes
    data=f.read(8)
    print(data)