f  = open('info.txt','r')
# f.seek(10)
print(f.tell())
# f.write(" this is at 10th the sensation of your destination")
print(f.read(5))
print(f.tell())
print(f.read(5))

f.close()