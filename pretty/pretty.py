
import matplotlib as mpl
import os 


class StyleFromFile:
    """ Base class for making matplotlib styles 
    from a file with rc params. 
    """

    def __init__(self, opts):
        rcfile = opts.get('rcfile', 'classicstyle')
        del opts['rcfile']
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), 
                                             os.path.dirname(__file__)))
        self.rcfile = f'{self.__location__}/styles/{rcfile}'
        self.opts = opts

    def __enter__(self):
        mpl.rc_file(self.rcfile)
        mpl.rcParams.update(self.opts)                        
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        mpl.rcParams.update(mpl.rcParamsDefault)
            


class LHCb(StyleFromFile):
    """ Plot using the LHCb style, courtesy of Kevin Dungs.
        https://github.com/kdungs/lhcb-matplotlibrc
        See /styles/lhcbstyle for detailed author information.
    """
    def __init__(self, useropts = {}):
        StyleFromFile.__init__(self, opts = {'rcfile':'lhcbstyle', **useropts})


class Classic(StyleFromFile):
    """ Plot using Classic style, courtesy of John Garrett
        https://github.com/garrettj403/ThesisPlots
    """
    def __init__(self, useropts = {}):
        StyleFromFile.__init__(self, opts = {'rcfile':'classicstyle', **useropts})        


class Monochrome(StyleFromFile):
    """ Plot using Monochrome style, courtesy of
    """
    def __init__(self, useropts = {}):
        StyleFromFile.__init__(self, opts = {'rcfile':'monochromestyle', **useropts})        


