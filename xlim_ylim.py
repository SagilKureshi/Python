import pylab as pl
from matplotlib.lines import lineStyles

x = [1,2,3,4,5]
y = [10,20,30,40,50]

pl.plot(x,y,'--',linewidth=5)
pl.show()
pl.plot(x,y,'red')
pl.show()
pl.title('Plot with color')
pl.xlabel("x axis")
pl.ylabel("y axis")
pl.xlim(0,6)
pl.ylim(0,60)
pl.show()