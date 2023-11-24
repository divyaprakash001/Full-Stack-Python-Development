import os
import time as t
os.chdir('Python 100')
folders = os.listdir('python100dayschallenge')
# print(folders)

# for folder in folders:
#     print(folder)


# files under folders
for folder in folders:
    print(folder)
    print(os.listdir(f"python100dayschallenge/{folder}"))
    t.sleep(0.3)