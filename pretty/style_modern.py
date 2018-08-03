
""" A simplistic modern layout
"""

from pretty.prettyStyle import *
from cycler import cycler


class style_modern(prettyStyle):
    """ Classic style for matplotlib.
    """

    FIXEDPARAMS = {'grid.color': 'k',
                   'grid.linestyle': '',
                   'grid.linewidth': 0.5,

                   'xtick.top': True,
                   'ytick.right': True,
                   'xtick.direction': 'in',
                   'ytick.direction': 'in',

                   'figure.dpi': 80,
                   'savefig.bbox': 'tight',
                   'axes.titlepad': 20.0,

                   'axes.titlesize': 'xx-large',
                   'axes.labelsize': 'x-large',
                   'axes.titlepad': 10.0,
                   'axes.grid': True}

    def __init__(self,
                palette = 'ponyo', tex = True, ubuntufont = False,
                figsize = (12.0, 8.0), save_dpi = 300, bgcolor =  '#FFFFF0'
                ):
        """ Initializes self and prettyStyle.

        Params:
            palette (='ponyo'): The palette to use
            tex (=True): Use tex in figures?
            ubuntufont (=False): use ubuntu font?
            figsize (=(12.0, 8.0)): size of figures.
            save_dpi (=300): dpi to use when saving figures.
            bgcolor (='white'): background color
        """

        # First we do a bunch of setup which is mostly default carried
        if ubuntufont:
            self.FIXEDPARAMS['font.family'] = 'Ubuntu'
        if tex:
            self.FIXEDPARAMS['text.usetex'] = True
            self.FIXEDPARAMS['font.family'] = 'serif'

        # background color
        self.FIXEDPARAMS['figure.facecolor']  = bgcolor
        self.FIXEDPARAMS['figure.edgecolor']  = bgcolor
        self.FIXEDPARAMS['axes.facecolor']    = bgcolor
        self.FIXEDPARAMS['savefig.edgecolor'] = bgcolor
        self.FIXEDPARAMS['savefig.facecolor'] = bgcolor

        # figure size
        self.FIXEDPARAMS['figure.figsize'] = [*figsize]
        self.FIXEDPARAMS['savefig.dpi'] = save_dpi


        prettyStyle.__init__(self, **self.FIXEDPARAMS)

        self.palette = palette
        mpl.rcParams['axes.prop_cycle'] = cycler('color', self._color_options[self.palette])
