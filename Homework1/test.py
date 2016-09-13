import matplotlib as mpl
mpl.use('svg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy import special as sps
from scipy.stats import laplace as l
import numpy as np
import math

#def normcdf(x):
#	return 0.5*(1+sps.erf(x/math.sqrt(2)))

x = np.linspace(-3,3,100)

plt.plot(x, l.pdf(x), linewidth=2.0, label='PDF')
plt.plot(x, l.cdf(x), linewidth=2.0, label='CDF')

#plt.plot(x, stats.laplace(x), linewidth=2.0, label='PDF')
#plt.plot(x, mlab.normpdf(x,0,1), linewidth=2.0, label='normal PDF')
#plt.plot(x, normcdf(x), linewidth=2.0, label='normal CDF')
plt.legend(bbox_to_anchor=(.35,1))
plt.savefig('cdf.svg', bbox_inches='tight')

