__author__='Royal Bhati'

#A simple GUI graph plotter in python3

import tkinter as tk
from functools import partial
import matplotlib.pyplot as plt
import numpy as np 


 
def graph_plot(label_x,label_y, n1, n2,graph_tit):
	xx=[]
	yy =[]
	
	pointxx=n1.get()
	pointyy=n2.get()

	for i in pointxx.split(','):
		xx.append(i) 
	for i in pointyy.split(','):
		yy.append(i) 	
	
	plt.plot(xx,yy)
	plt.xlabel(label_x.get())
	plt.ylabel(label_y.get())
	plt.title(graph_tit.get())
	plt.grid(True)
	plt.savefig("GRAPH.png")
	plt.show()
	
 
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Graph Plotter')
 
point1 = tk.StringVar()
point2 = tk.StringVar()
l_x = tk.StringVar()
l_y=tk.StringVar()
g_t=tk.StringVar()
labelTitle = tk.Label(root, text="Simple Graph Plotter").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter points to be plotted in x direction").grid(row=3, column=0)
labelNum2 = tk.Label(root, text="Enter points to be plotted in y direction").grid(row=6, column=0)
labelofx = tk.Label(root, text="Enter the display label for x direction").grid(row=2, column=0)
labelofy = tk.Label(root, text="Enter the display level for y direction").grid(row=4, column=0)
labelofgraph= tk.Label(root, text="Enter the title of the graph").grid(row=1, column=0)

 
entryNum1 = tk.Entry(root, textvariable=point1).grid(row=3, column=2)
entryNum2 = tk.Entry(root, textvariable=point2).grid(row=6, column=2)
lofx = tk.Entry(root, textvariable=l_x).grid(row=2, column=2)
lofy = tk.Entry(root, textvariable=l_y).grid(row=4, column=2)
lofg =tk.Entry(root, textvariable=g_t).grid(row=1, column=2)

graph_plot = partial(graph_plot,l_x,l_y, point1, point2,g_t)
buttonCal = tk.Button(root, text='Plot Graph', command=graph_plot).grid(row=7, column=0)
root.mainloop()
