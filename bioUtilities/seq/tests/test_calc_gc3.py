from bioUtilities.seq import calc_gc3
import unittest
import numpy as np

class TestCalcGC3(unittest.TestCase):

    def test_calc_gc3(self):
        sequence = "TACGATCGCGCATATCGAGCTCTAGAGCGCTAGAGCTCTAGC"
        observed = calc_gc3(sequence)
        self.assertEqual(observed, np.divide(7, 14))
