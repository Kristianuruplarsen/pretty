import numpy as np
import matplotlib.pyplot as plt
import cmocean

from pretty.pretty import *


style = pretty('totoro')


style.palette = 'ponyo'



import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.linspace(0,10), np.sqrt(np.linspace(0,10)))
plt.show()



# ------------------------------------------------------------------------------
# Example 1: sigmoid lines
style.style_classic()

def sigmoid(z, c):
    return c/(1 + np.exp(-z))

sig_fn = np.vectorize(sigmoid)

x = np.arange(-10, 10, .01)
y =  sig_fn(x, 3)

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



# ------------------------------------------------------------------------------
# Example 3: continous variable
from matplotlib.colors import LinearSegmentedColormap

cm = LinearSegmentedColormap.from_list('test', ["#5f8bcc","#3069c2","#2f4337","#4e693c","#77a66f","#8f3535","#a7784e","#985d32","#e2d234","#d9db6e"], N=100)

x = y = np.linspace(0,10, 100)

def f(x,y):
    return np.sqrt(x*y)

X,Y = np.meshgrid(x, y)
Z = np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(X.shape[0]):
        Z[i,j] = f(X[i,j], Y[i,j])

plt.pcolor(X,Y,Z, cmap = cm)
plt.show()
