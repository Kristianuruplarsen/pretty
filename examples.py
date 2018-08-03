import numpy as np
import matplotlib.pyplot as plt
import cmocean
from pretty import style_classic

# ------------------------------------------------------------------------------
# Example 1: sigmoid lines
style_classic('ponyo')

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
# Example 3: colormaps
s = style_classic('nausicaa')


x = np.linspace(0,10, 200)
y = np.linspace(0,10, 200)

def f(x, y):
    return np.sqrt(x*y)

X, Y = np.meshgrid(x,y)
Z = np.zeros(X.shape)

for i in range(X.shape[0]):
   for j in range(X.shape[0]):
       Z[i,j] = f(X[i,j],Y[i,j])


f, (ax1, ax2) = plt.subplots(1,2, sharey = True)
ax1.pcolor(X, Y, Z, cmap = s.cm.full)
ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$y$")
ax1.set_title(r"\texttt{cmap = s.cm.full}")

ax2.pcolor(X, Y, Z, cmap = s.cm.binary)
ax2.set_xlabel(r"$x$")
ax2.set_ylabel(r"$y$")
ax2.set_title(r"\texttt{cmap = s.cm.binary}")

plt.suptitle(r"$\sqrt{x\cdot y}$ with theme 'nausicaa'")

plt.savefig('example_figures/colormaps.png')
plt.show()







x = np.linspace(0,10, 200)
y = np.linspace(0,10, 200)

def f(x, y):
    return np.exp(x*y)

X, Y = np.meshgrid(x,y)
Z = np.zeros(X.shape)

for i in range(X.shape[0]):
   for j in range(X.shape[0]):
       Z[i,j] = f(X[i,j],Y[i,j])


with style_classic('ponyo') as s:

    f, ax1 = plt.subplots(1,1)
    ax1.pcolor(X, Y, Z, cmap = s.cm.full)
    ax1.set_xlabel(r"$x$")
    ax1.set_ylabel(r"$y$")
    ax1.set_title(r"$e^{x*y}$ (\texttt{cmap = s.cm.full})")

    plt.savefig('example_figures/colormaps_with.png')
    plt.show()
