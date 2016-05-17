import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
pullData = open("twittersent.txt","r").read()
lines = pullData.split('\n')
x = 0
y = 0

for l in lines[-200:]:
    
    if "pos" in l:
       x += 1
    elif "neg" in l:
       y += 1
# The slices will be ordered and plotted counter-clockwise.
labels ='-', '+'
sizes = [x,y]
colors = ['yellowgreen', 'gold']
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
	# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

#fig = plt.figure()
plt.show()

        	








	
