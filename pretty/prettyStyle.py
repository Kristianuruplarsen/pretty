

""" PRETTY - a few classes for increased beauty of matplotlib plots.
This is the main prettyStyle class, and classes for each of it's derivatives.
"""

import warnings
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap


from pretty.utils import *


class prettyStyle:
    """ Base style class - set up the inner working shared by all of the styles.
    Not for end users.

    Params:
        **kwargs: a dictionary of rcParams passed to matplotlib.
    """

    def __init__(self, **kwargs):

        # always begin by resetting style
        style_reset()

        self._color_options = {
        'classic': 'bgrcmyk',
        'castle_in_the_sky': ["#5f8bcc","#3069c2","#2f4337","#4e693c","#77a66f","#8f3535","#a7784e","#985d32","#e2d234","#d9db6e"],
        'kiki_delivery_service': ["#3f97a3","#2188a7","#1d3e6b","#19479d","#8e9753","#d4d770","#3f406e","#cab9b2","#2b0908","#c53840"],
        'the_wind_rises': ["#f0c4a7","#f1c8aa","#cfacb3","#f8e5ad","#16a13a","#ece3d4","#1baa41","#007db3","#008fbb","#0096c3"],
        'totoro': ["#876c57","#473535","#ece3d4","#82c1ed","#f38524","#fcf95e","#fefc8d","#5096eb","#fefec2","#567442"],
        'princess_mononoke': ["#171916","#473535","#a79297","#6a5157","#8898b1","#efefef","#4c5119","#eebca1","#e07d6a","#bc3d36"],
        'nausicaa': ["#002627","#556a59","#6e6046","#deacab","#f5f1e6","#ffea81","#fbe5b3","#dce4cf","#36b3df","#0598ce"],
        'ponyo': ["#dcedff","#25387c","#37458e","#304795","#5284c3","#62a0dd","#80b5df","#651025","#994264","#b03d36"]
        }

        # Set the layout rcParams
        for k,v in kwargs.items():

            if not k in mpl.rcParams:
                warnings.warn(f"{k} is not a valid rcParam. Skipped.")
            else:
                mpl.rcParams[k] = v

        # Storage for chosen palette
        self._palette = False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.palette})"

    def __str__(self):
        return f"{self.__class__.__name__} style with palette {self.palette}"

    def __enter__(self):
            return self

    def __exit__(self, exception_type, exception_value, traceback):
            style_reset()


    class _cm:
        """ colormap internal class. Generates the two available colormaps as
        attributes. Not for end users, is called within the prettyStyle class only.

        Params:
            colors: A list of colors to create cmap from.
        """
        def __init__(self, colors):
            self._b = (colors[0], colors[-1])
            self._f = colors

        @property
        def binary(self):
            """ Binary color map.
            """
            return LinearSegmentedColormap.from_list('binary', self._b, N=250)

        @property
        def full(self):
            """ Full color map.
            """
            return LinearSegmentedColormap.from_list('full', self._f, N=250)


    @property
    def cm(self):
        """ Exposes the _cm class to the end user. This is the access point for
        using the colormaps.
        """
        return self._cm(self._color_options[self.palette])

    @property
    def palette(self):
        """ palette getter - can be any palette available in the color_options.
        """
        if not self._palette:
            raise ValueError('No palette set.')
        return self._palette

    @palette.setter
    def palette(self, palette):
        """ Palette setter
        """
        if not palette in self._color_options:
            raise ValueError(f"Palette {palette} is not a valid palette.")
        self._palette = palette


    @property
    def color_options(self):
        """ Color options setter
        """
        return list(self._color_options.keys())
