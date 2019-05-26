from utilities.seq import calc_gc
import unittest

class TestCalcPurine(unittest.TestCase):

    def test_calc_gc(self):
        sequence = "ACATCGACTTGCTTA"
        observed = calc_gc(sequence)
        self.assertEqual(observed, 0.4)
