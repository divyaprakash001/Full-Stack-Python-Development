import matplotlib.pyplot as p
import numpy as np

y = np.array([3,8,1,10])

# marker/line/color
p.plot(y,'D-.r', ms='10')  #ms marker size 
# p.plot(y,marker='D', ms='10',mec='b', mfc='r')  #ms marker size #mec marker color
# p.plot(y,marker='D', ms='10',mec='#82affa', mfc='#42f6ad')  #ms marker size #mec marker color
# p.plot(y,marker='D',linestyle='dotted', ms='10',mec='#82affa', mfc='#42f6ad')  #ms marker size #mec marker color
# p.plot(y,marker='D',linestyle='dashed', ms='10',mec='#82affa', mfc='#42f6ad')  #ms marker size #mec marker color
# p.plot(y,marker='D',ls='-.', ms='10',mec='#82affa', mfc='#42f6ad')  #ms marker size #mec marker color
# p.plot(y,marker='D',ls='-.',c='orange', ms='10',mec='#82affa', mfc='#42f6ad')  #ms marker size #mec marker color
p.plot(y,marker='D',ls='-', linewidth='15.5'  ,c='orange', ms='10',mec='#82affa', mfc='#42f6ad')  #ms marker size #mec marker color

p.show()