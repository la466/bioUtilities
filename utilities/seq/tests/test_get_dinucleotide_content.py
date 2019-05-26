from utilities.seq import get_dinucleotide_content
import unittest
import numpy as np

class TestGetDinucleotideContent(unittest.TestCase):

    def test_calc_gc4(self):
        sequence = "GACTGA"
        observed = get_dinucleotide_content(sequence)
        expected = {'AC': 0.2, 'CT': 0.2, 'GA': 0.4, 'TG': 0.2}
        self.assertEqual(observed, expected)
