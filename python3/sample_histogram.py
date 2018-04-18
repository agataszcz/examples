#!/usr/bin/env python
'''A sample histogram'''

import matplotlib.pyplot as plt

#sample data
population_ages = [2,35,40,55,68,109,11,15,26,56,78,90,105,38,44,45,65,39,45,49,50,47,69,77,89,34,67,23,14,25,60,34,99]

bins = [0,10,20,30,40,50,60,70,80,90,100,110]

#plot the histogram
plt.hist(population_ages,bins, histtype = 'bar',rwidth=0.8, color= 'g')
plt.xlabel('Age')
plt.ylabel('y')
plt.title("Sample Histogram: Age Distribution")
plt.show()