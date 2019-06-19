from bioUtilities.seq import calc_gc4
import unittest
import numpy as np

class TestCalcGC4(unittest.TestCase):

    def test_calc_gc4(self):
        sequence = "ACAGCTACGACGATCGACGATCAGCTACTAGCATGAG"
        observed = calc_gc4(sequence)
        self.assertEqual(observed, 0.4)

        sequence = "GTTGTAGTGCCACCG"
        observed = calc_gc4(sequence)
        self.assertEqual(observed, 0.4)
