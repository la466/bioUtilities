from bioUtilities.sim import dinucleotide_matched
import unittest

class TestDinucleotideMatched(unittest.TestCase):

    def test_dinucleotide_matched(self):
        sequence = "ACATCA"
        observed = dinucleotide_matched(sequence, seed = 1)
        expected = "CACAAC"
        self.assertEqual(observed, expected)

    def test_dinucleotide_matched_list(self):
        sequences = ["ACATCA", "ACGGACTA"]
        observed = dinucleotide_matched(sequences, seed = 1)
        expected = ["CAGAAC", "ATACACAC"]
        self.assertEqual(observed, expected)
