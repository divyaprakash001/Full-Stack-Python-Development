wr = open('./myworld.txt','w')
wr.writelines(''' Hey! I am divya prakash
              my father name id mr deepak kumar ''')
wr.flush()

wr  = open('E:\\Python Full Stack Development\\Python 100\\File_IO\\myfile.txt','w')
wr.writelines(''' Hey! I am divya prakash.
my father name id mr deepak kumar ''')

wr.close()