from bioUtilities.seq import calc_dinucleotide
import unittest
import numpy as np

class TestCalcDinucleotide(unittest.TestCase):

    def test_calc_dinucleotide(self):
        sequence = "GACTGA"
        observed = calc_dinucleotide(sequence)
        expected = {'AC': 0.2, 'CT': 0.2, 'GA': 0.4, 'TG': 0.2}
        self.assertEqual(observed, expected)

    def test_calc_dinucleotide_list(self):
        sequences = ["ACGAT", "ACTAG"]
        observed = calc_dinucleotide(sequences)
        expected = {"AC": 0.25, "AG": 0.125, "AT": 0.125, "CG": 0.125, "CT": 0.125, "GA": 0.125, "TA": 0.125}
        self.assertEqual(observed, expected)
