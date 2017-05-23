"""
Example module
"""
class test1:
    """demo class 1"""

    def __init__(self):
        """ BLERG

        *lorem ipsum lorem ipsum*
        **lorem ipsum lorem ipsum**
        lorem ipsum lorem ipsum

        lorem ipsum lorem ipsum
        """
        print 'initialized.'

    def someFunc(self,a,b,c):
        """ FOO

        Parameters
        ----------
        a : string
            asdf
        b : int
            jkl
        c : float
            12345
        """
        print 'do something'

    def someOtherFunc(self,d,e,f):
        """ BAR

        Parameters
        ----------
        d : string
            ghjkl
        e : int, optional
            67890
        f : float, optional
            qwerty
        """
        print 'do something else'

class test2:
    """demo class 2"""
    def __init__(self):
        """ Another class.
        """
        print 'initialized.'
