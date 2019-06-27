from bioUtilities.seq import calc_nucleotide
import unittest
import numpy as np

class TestCalcNucleotide(unittest.TestCase):

    def test_calc_nucleotide(self):
        sequence = "GACTG"
        observed = calc_nucleotide(sequence)
        expected = {'A': 0.2, 'C': 0.2, 'G': 0.4, 'T': 0.2}
        self.assertEqual(observed, expected)

    def test_calc_nucleotide_list(self):
        sequences = ["ACGAT", "ACTAG"]
        observed = calc_nucleotide(sequences)
        expected = {"A": 0.4, "C": 0.2, "G": 0.2, "T": 0.2}
        self.assertEqual(observed, expected)
