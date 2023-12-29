import matplotlib.pyplot as t
import numpy as p

x = p.array([0,2,4,7,9,10,11,12,15])
y = p.array([0,2,5,7,9,4,9,15,31])
# t.plot(x,y,'o')
# t.plot(x,y)
# t.plot(y,marker='*')
# t.plot(x,y,'o-r')
# t.plot(x,y,'o:r')
# t.plot(x,y,'o-.r')
# t.plot(x,y,'o:r')
t.plot(x,y,'o:r',ms=22)
t.show()