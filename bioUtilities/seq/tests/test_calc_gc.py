from utilities.seq import calc_gc
import unittest

class TestCalcGC(unittest.TestCase):

    def test_calc_gc(self):
        sequence = "ACTAGCAGCTAGCAGCATCAGCGACATCGACGACTGACGA"
        observed = calc_gc(sequence)
        self.assertEqual(observed, 0.55)
