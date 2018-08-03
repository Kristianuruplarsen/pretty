
""" Utilities for the pretty module.
"""

import matplotlib as mpl

def style_reset():
    """ Reset the style sheet to matplotlibs default.
    """
    mpl.rcParams.update(mpl.rcParamsDefault)
