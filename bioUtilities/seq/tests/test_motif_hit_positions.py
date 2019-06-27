from bioUtilities.seq import motif_hit_positions
import unittest
import numpy as np

class TestMotifHitPositions(unittest.TestCase):

    def test_motif_hit_positions(self):
        sequence = "ACATCGACTTGCTTA"
        motifs = ["CAT", "TTA"]
        observed = motif_hit_positions(sequence, motifs)
        expected = [1, 2, 3, 12, 13, 14]
        self.assertEqual(observed, expected)
