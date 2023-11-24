with open('E:\\Python Full Stack Development\\Python 100\\File_IO\\file.txt','r') as f:
    # read first 10 bytes
    data = f.read(13)
    print(data)

    # save the curremt position
    currentPosition = f.tell()
    print(currentPosition)

    # seek the saved position
    f.seek(currentPosition)