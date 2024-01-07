import sys
# for arg in sys.argv[1:]:
for arg in ['info.txt','ready.txt','emp.txt'][:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

