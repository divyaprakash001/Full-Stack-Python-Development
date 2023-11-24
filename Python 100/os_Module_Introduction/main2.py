import os

print(os.getcwd())
os.chdir('Python 100')
print(os.getcwd())

if not os.path.exists('python100dayschallenge'):
    os.mkdir('python100dayschallenge')

for i in range(0,100):
    os.mkdir(f"python100dayschallenge/Day{i+1}")