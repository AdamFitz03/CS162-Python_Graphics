import matplotlib.pyplot as plot
# set up your lists
numlist = [10, 6, 5, 3]
namelist = ['Adam', 'Not Adam', 'James', 'Also Not Adam']
colorlist = ['lightsalmon', 'tomato', 'peru', 'darkkhaki' ]
explodelist = [0.04, 0.03, 0.02, 0.01]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 60)
plot.axis('equal')
plot.savefig('piechart.png')
