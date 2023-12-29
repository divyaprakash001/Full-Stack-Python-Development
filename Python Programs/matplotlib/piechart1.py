import matplotlib.pyplot as t
import numpy as p

# x = p.array([0,2,4,7,9,10,11,12,15])
t.title('line')
t.xlabel('x-coordinate')
t.ylabel('y-coordinate')
y1 = p.array([0,2,4,7,9,10,11,12,15])
y2 = p.array([0,1,2,3,4,5,6,9,15,31])

t.plot(y1,'o:g',ms=9)
t.plot(y2,'*-b',ms=10)
t.show()