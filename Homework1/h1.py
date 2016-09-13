import matplotlib as mpl
mpl.use('svg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import laplace as l
import numpy as np
import math

x = np.linspace(-3,3,100)

plt.plot(x, l.pdf(x), linewidth=2.0, label='PDF')
plt.plot(x, l.cdf(x), linewidth=2.0, label='CDF')

plt.legend(bbox_to_anchor=(.35,1))
plt.savefig('cdf.svg', bbox_inches='tight')

