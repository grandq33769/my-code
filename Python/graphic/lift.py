'''
Created on 2017�?4???10?��

@author: LokHim
'''
from matplotlib import cm

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # @UnresolvedImport
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

confidence = np.arange(0.1, 1, 0.1)
probability_of_left = np.arange(0.1, 1, 0.1)
confidence, probability_of_left = np.meshgrid(confidence, probability_of_left)
lift = confidence / probability_of_left

surf = ax.plot_surface(confidence, probability_of_left,
                       lift, cmap=cm.YlGnBu, linewidth=0, antialiased=False)
ax.set_xlabel('Confidence')
ax.set_ylabel('Probability of left')
ax.set_zlabel('Lift')
ax.set_zlim(0, 10)

plt.title('Change of Lift')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()