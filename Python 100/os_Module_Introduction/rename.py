import os
os.chdir('Python 100')
for i in range(0,100):
    os.rename(f"python100dayschallenge/Day{i+1}",f"python100dayschallenge/Tutorial{i+1}")