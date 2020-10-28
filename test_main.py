import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xvalues(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        myy = np.loadtxt("bubbles.dat")
        self.assertTrue( len(this_x)==200, "the number of coordinates you have plotted on the graph is wrong" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "The x coordinates in your plot are incorrect" )
            self.assertTrue( np.abs( (4/3)*np.pi*myy[i]*myy[i]*myy[i] - this_y[i])<1e-7, "the y coordinates of your plot are not correct" )
            
