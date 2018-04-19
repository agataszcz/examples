#!/usr/bin/env python
'''Sample histogram: normal distribution'''

import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

g_height = 28 + 4 * np.random.randn(greyhounds)
#28 = mean. Points will be centered on 28. 4 is the degree of spread (average distance from the mean).
#Randn choses points according to normal distribution, not just randomly.
l_height = 24 + 4 * np.random.randn(labs)


plt.hist([g_height, l_height], stacked=True, color=['tab:orange', 'g'], rwidth=0.9)
plt.xlabel('Height in Inches')
plt.ylabel('Samples')
plt.show()