# pretty

This is my attempt at a simple, yet usable matplotlib style. So far it's just a few functions, the most important being `style_classic` which produces relatively neutral figures. Simply call the function at the beginning of your script, and it will update the rcParams needed. A full list of functions is

* `style_classic` - sets the classic style shown below
* `style_reset` - resets the style to the default matplotlib color_options
* `style_modern` - under development.

# Installation
Comming soon


# Colorschemes
There is a number of colorschemes available, all based on the ghibli-studio inspired schemes shown [here](https://www.hotfootdesign.co.uk/white-space/the-colour-palettes-of-studio-ghibli-animations-by-designer-hyo-taek-kim/). Available schemes are


* `classic` (v1 matplotlib colors)
* `castle_in_the_sky`
* `kiki_delivery_service`
* `the_wind_rises`
* `totoro`
* `princess_mononoke`
* `nausicaa`
* `ponyo`

# `style_classic` examples
 Here are some examples of what can be made with `style_classic`:

## Sigmoids
This figure uses the _ponyo_ colorscheme, and is otherwise fully standard settings. The code required to produce the figure is

```python
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
plt.grid()
```

 <p align="center">
 <img src="example_figures/sigmoid.png" alt="sigmoid functions">
 </p>  



## Heterogeneous errors scatterplot
This also features the `style_classic` function, but uses the (default) _totoro_ color scheme. The code used is

```python
style_classic('totoro')

x = np.arange(-10,10,0.2)
y = 3*x

for c in range(1,5):
    plt.scatter(x,y + np.random.normal(int(20/0.2), scale = c*abs(x)), label = r"$\varepsilon \sim \mathcal{N}(0, \ $" + str(c) + "$\cdot x)$")
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel(r"$y = 3x + \varepsilon$")
plt.title('Heterogeneous noise')
plt.savefig('example_figures/hetero.png')
plt.show()
```

<p align="center">
<img src="example_figures/hetero.png" alt="sigmoid functions">
</p>  
