import matplotlib.pyplot as t
import numpy as p

# x = p.array([0,2,4,7,9,10,11,12,15])
y1 = p.array([0,2,5,7,9,4,9,15,31])
y2 = p.array([0,1,2,3,4,5,6,9,15,31])
# t.plot(x,y,'o')
# t.plot(x,y)
# t.plot(y,marker='*')
# t.plot(x,y,'o-r')
# t.plot(x,y,'o:r')
# t.plot(x,y,'o-.r')
# t.plot(x,y,'o:r')
t.plot(y1,'o:g',ms=9)
t.plot(y2,'*-b',ms=10)
t.show()