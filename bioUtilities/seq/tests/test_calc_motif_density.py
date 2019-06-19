from bioUtilities.seq import calc_motif_density
import unittest
import numpy as np

class TestCalcMotifDensity(unittest.TestCase):

    def test_calc_motif_density_single(self):
        sequence = "TACGACAGCATCAAC"
        observed = calc_motif_density(sequence, ["TAC", "CAG"])
        self.assertEqual(observed, 0.4)

    def test_calc_motif_density_list(self):
        sequences = ["TACGACAGCATCAAC", "TGCGAGATAC", "TGAAATTCAGC"]
        observed = calc_motif_density(sequences, ["TAC", "CAG"])
        self.assertEqual(observed, np.divide(12, 36))
