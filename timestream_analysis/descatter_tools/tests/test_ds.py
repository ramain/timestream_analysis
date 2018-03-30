import numpy as np
from astropy.tests.helper import catch_warnings
from timestream_analysis.descatter_tools.descatter_tools import *

class TestDS(object):

    def test_rechannelize(self):
        ts = np.random.normal(size=(2**10, 17))
        dchan = dechannelize(ts)
        print(dchan.shape)
        assert (dchan.shape[0]==2**15)

