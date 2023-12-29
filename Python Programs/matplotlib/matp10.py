import matplotlib.pyplot as p
import numpy as np

y1 = np.array([3,8,9,10])
y2 = np.array([1,2,5,7,1,10])
x1 = np.array([1,5,9,12])
x2 = np.array([1,4,7,9,11,13])

# marker/line/color
p.plot(x1,y1,x2,y2,'*-r') 

p.title('line chart')
p.xlabel('avrage')
p.ylabel('donate')

# p.grid(axis='x')
# p.grid(axis='y')
p.grid()



p.show()