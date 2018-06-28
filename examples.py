import numpy as np
import matplotlib.pyplot as plt

from pretty.pretty import style_classic, style_modern

import matplotlib as mpl
# ------------------------------------------------------------------------------
# Example 1: sigmoid lines
style_classic('ponyo')

#style_modern('ponyo')

def sigmoid(z, c):
    return c/(1 + np.exp(-z))

sig_fn = np.vectorize(sigmoid)

x = np.arange(-10, 10, .01)
y =  sig_fn(x, 3)

# mpl.rcParams['axes.spines.top'] = True
# mpl.rcParams['axes.spines.bottom'] = False
# mpl.rcParams['axes.spines.left'] = True
# mpl.rcParams['axes.spines.right'] = False
# mpl.rcParams['axes.grid'] = False
#
# mpl.rcParams['xtick.top'] = True
# mpl.rcParams['ytick.right'] = False
# mpl.rcParams['xtick.bottom'] = False
#

for c in range(1,11):
    plt.plot(x,sig_fn(x, np.sqrt(c)), label = 'c=' + str(c))
plt.title('Sigmoid functions')
plt.legend()
plt.ylabel(r"$\frac{c}{1 + e^{-z}}$")
plt.xlabel('z')
plt.savefig('example_figures/sigmoid.png')
plt.show()




# ------------------------------------------------------------------------------
# Example 2: scatter
style_classic('totoro')

x = np.arange(-10,10,0.2)
y = 3*x


for c in range(1,5):
    plt.scatter(x,y + np.random.normal(int(20/0.2), scale = c*abs(x)), label = r"$\varepsilon \sim \mathcal{N}(0, \ $" + str(c) + "$\cdot x)$")
plt.legend()
plt.xlabel('x')
plt.ylabel(r"$y = 3x + \varepsilon$")
plt.title('Heterogeneous noise')
plt.savefig('example_figures/hetero.png')
plt.show()
