#!/usr/bin/env python
'''A sample bar chart'''

import matplotlib.pyplot as plt

#sample bar 1
x = [2,4,6,8,10]
y = [6,7,8,5,6]

plt.bar(x,y, label = "Bar 1", color = 'c')

#sample bar 2
x2 = [1,3,5,7,9]
y2 = [3,5,6,4,8]

plt.bar(x2,y2,label = "Bar 2", color = 'b')

#plot the graph and describe it
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Simple Bar Charts")
plt.show()