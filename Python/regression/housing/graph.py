'''
Created on 2017�?4???12?��

@author: LokHim
'''
from housing import data_input as di

import matplotlib.pyplot as plt
import numpy as np
import pylab as mpl

# Chinese Chracter
mpl.rcParams['font.sans-serif'] = ['heit']
mpl.rcParams['axes.unicode_minus']

# my result : weight:-0.95 bias: 34.54
# my result 2 : weight:-2.3272 weight2:0.0434 bias:42.8169

x = np.arange(0, 40)
y = -0.95 * x + 34.54
y2 = -2.3272 * x + 0.0434 * x**2 + 42.8169

plt.xlabel(di.attribute_name[di.input_attribute_index])
plt.ylabel(di.attribute_name[di.target_attribute_index])
for member in di.target_list:
    plt.scatter(member[0], member[1], color='blue')
plt.plot(x, y, 'r')
plt.plot(x, y2, color='#D9B611')
plt.title(u'中�??')

plt.show()