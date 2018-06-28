# pretty

This is my attempt at a simple, yet usable matplotlib style. So far it's just one function, `style_classic` which produces relatively neutral figures. Simply call the function at the beginning of your script, and it will update the rcParams needed.

# Installation
Comming soon


# Colorschemes
There is a number of colorschemes available, all based on the ghibli-studio inspired schemes shown [here](https://www.hotfootdesign.co.uk/white-space/the-colour-palettes-of-studio-ghibli-animations-by-designer-hyo-taek-kim/). Available schemes are


* `classic` (v1 matplotlib colors)
* `castle_in_the_sky` (<font color=#5f8bcc>  &#9632; </font>,<font color=#3069c2>  &#9632; </font>,<font color=#2f4337>  &#9632; </font>,<font color=#4e693c>  &#9632; </font>,<font color=#77a66f>  &#9632; </font>,<font color=#8f3535>  &#9632; </font>,<font color=#a7784e>  &#9632; </font>,<font color=#985d32>  &#9632; </font>,<font color=#e2d234>  &#9632; </font>,<font color=#d9db6e>  &#9632; </font>)
* `kiki_delivery_service` (<font color=#3f97a3>  &#9632; </font>,<font color=#2188a7>  &#9632; </font>,<font color=#1d3e6b>  &#9632; </font>,<font color=#19479d>  &#9632; </font>,<font color=#8e9753>  &#9632; </font>,<font color=#d4d770>  &#9632; </font>,<font color=#3f406e>  &#9632; </font>,<font color=#cab9b2>  &#9632; </font>,<font color=#2b0908>  &#9632; </font>,<font color=#c53840>  &#9632; </font>)
* `the_wind_rises` (<font color=#f0c4a7>  &#9632; </font>,<font color=#f1c8aa>  &#9632; </font>,<font color=#cfacb3>  &#9632; </font>,<font color=#f8e5ad>  &#9632; </font>,<font color=#16a13a>  &#9632; </font>,<font color=#ece3d4>  &#9632; </font>,<font color=#1baa41>  &#9632; </font>,<font color=#007db3>  &#9632; </font>,<font color=#008fbb>  &#9632; </font>,<font color=#0096c3>  &#9632; </font>)
* `totoro` (<font color=#876c57>  &#9632; </font>,<font color=#473535>  &#9632; </font>,<font color=#ece3d4>  &#9632; </font>,<font color=#82c1ed>  &#9632; </font>,<font color=#f38524>  &#9632; </font>,<font color=#fcf95e>  &#9632; </font>,<font color=#fefc8d>  &#9632; </font>,<font color=#5096eb>  &#9632; </font>,<font color=#fefec2>  &#9632; </font>,<font color=#567442>  &#9632; </font>)
* `princess_mononoke` (<font color=#171916>  &#9632; </font>,<font color=#473535>  &#9632; </font>,<font color=#a79297>  &#9632; </font>,<font color=#6a5157>  &#9632; </font>,<font color=#8898b1>  &#9632; </font>,<font color=#efefef>  &#9632; </font>,<font color=#4c5119>  &#9632; </font>,<font color=#eebca1>  &#9632; </font>,<font color=#e07d6a>  &#9632; </font>,<font color=#bc3d36>  &#9632; </font>)
* `nausicaa` (<font color=#002627>  &#9632; </font>,<font color=#556a59>  &#9632; </font>,<font color=#6e6046>  &#9632; </font>,<font color=#deacab>  &#9632; </font>,<font color=#f5f1e6>  &#9632; </font>,<font color=#ffea81>  &#9632; </font>,<font color=#fbe5b3>  &#9632; </font>,<font color=#dce4cf>  &#9632; </font>,<font color=#36b3df>  &#9632; </font>,<font color=#0598ce>  &#9632; </font>)
* `ponyo` (<font color=#dcedff>  &#9632; </font>,<font color=#25387c>  &#9632; </font>,<font color=#37458e>  &#9632; </font>,<font color=#304795>  &#9632; </font>,<font color=#5284c3>  &#9632; </font>,<font color=#62a0dd>  &#9632; </font>,<font color=#80b5df>  &#9632; </font>,<font color=#651025>  &#9632; </font>,<font color=#994264>  &#9632; </font>,<font color=#b03d36>  &#9632; </font>)


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
