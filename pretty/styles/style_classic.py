from cycler import cycler
import matplotlib as mpl

from pretty.utils import *

def style_classic(
                  palette = 'the_wind_rises', tex = True, ubuntufont = False,
                  figsize = (12.0, 8.0), save_dpi = 300, bgcolor = 'white'
                  ):
    """ A classical easy-on-the-eyes graph layout which is not to fancy.
    """

    style_reset()

    color_options = {
    'classic': 'bgrcmyk',
    'castle_in_the_sky': ["#5f8bcc","#3069c2","#2f4337","#4e693c","#77a66f","#8f3535","#a7784e","#985d32","#e2d234","#d9db6e"],
    'kiki_delivery_service': ["#3f97a3","#2188a7","#1d3e6b","#19479d","#8e9753","#d4d770","#3f406e","#cab9b2","#2b0908","#c53840"],
    'the_wind_rises': ["#f0c4a7","#f1c8aa","#cfacb3","#f8e5ad","#16a13a","#ece3d4","#1baa41","#007db3","#008fbb","#0096c3"],
    'totoro': ["#876c57","#473535","#ece3d4","#82c1ed","#f38524","#fcf95e","#fefc8d","#5096eb","#fefec2","#567442"],
    'princess_mononoke': ["#171916","#473535","#a79297","#6a5157","#8898b1","#efefef","#4c5119","#eebca1","#e07d6a","#bc3d36"],
    'nausicaa': ["#002627","#556a59","#6e6046","#deacab","#f5f1e6","#ffea81","#fbe5b3","#dce4cf","#36b3df","#0598ce"],
    'ponyo': ["#dcedff","#25387c","#37458e","#304795","#5284c3","#62a0dd","#80b5df","#651025","#994264","#b03d36"]
    }

    if ubuntufont:
        mpl.rcParams['font.family'] = 'Ubuntu'

    if tex:
        mpl.rcParams['text.usetex'] = True
        mpl.rcParams['font.family'] = 'serif'

    mpl.rcParams['grid.color'] = 'k'
    mpl.rcParams['grid.linestyle'] = ':'
    mpl.rcParams['grid.linewidth'] = 0.5

    mpl.rcParams['xtick.top'] = True
    mpl.rcParams['ytick.right'] = True
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'

    mpl.rcParams['axes.prop_cycle'] = cycler('color', color_options[palette])

    # background color
    mpl.rcParams['figure.facecolor'] = bgcolor
    mpl.rcParams['figure.edgecolor'] = bgcolor
    mpl.rcParams['axes.facecolor'] = bgcolor

    mpl.rcParams['savefig.edgecolor'] = bgcolor
    mpl.rcParams['savefig.facecolor'] = bgcolor

    # figure size
    mpl.rcParams['figure.figsize'] = [*figsize]
    mpl.rcParams['figure.dpi'] = 80
    mpl.rcParams['savefig.dpi'] = save_dpi
    mpl.rcParams['savefig.bbox'] = 'tight'
    mpl.rcParams['axes.titlepad'] = 20.0

    mpl.rcParams['axes.titlesize'] = 'xx-large'
    mpl.rcParams['axes.labelsize'] = 'x-large'
    mpl.rcParams['axes.titlepad'] = 10.0
    mpl.rcParams['axes.grid'] = True
