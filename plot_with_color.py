import pylab as pl
x = [1,2,3,4,5,6]
y = [1,5,1,5,1,5]

pl.plot(x,y,'--','lightblue',linewidth=5)
pl.show()
pl.plot(x,y,'red')
pl.show()
pl.title('Plot with color')
pl.xlabel("x axis")
pl.ylabel("y axis")
pl.show()