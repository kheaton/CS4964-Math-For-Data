import matplotlib as mpl
#mpl.use(’PDF’)
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.special as sps
import numpy as np
import math
# no built-in normalcdf, but erf() is cdf of signed Gaussian error,
# cdf of (1/sqrt(2 pi)) exp(-xˆ2), but shifted to pass through (0,0)
def normcdf(x):
    return 0.5*(1 + sps.erf(x/math.sqrt(2)))
    
x = np.linspace(-3, 3, 100)
plt.plot(x, mlab.normpdf(x, 0, 1),linewidth=2.0, label='normalPDF')
plt.plot(x, normcdf(x),linewidth=2.0, label='normal CDF')
plt.legend(bbox_to_anchor=(.35,1))
plt.savefig('normal.pdf', bbox_inches='tight')
