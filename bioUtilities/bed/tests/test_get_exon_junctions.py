from bioUtilities.bed import MODULE_DIR, get_exon_junctions
from bioUtilities.files import read_many_fields, remove_file
import unittest

class TestGetExonJunctions(unittest.TestCase):

    def test_get_exon_junctions1(self):
        input_file = "{0}/tests/data/input_coding_exons.bed".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_get_exon_junctions1.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_get_exon_junctions1.bed".format(MODULE_DIR)
        remove_file(observed_file)
        get_exon_junctions(input_file, observed_file)
        observed = read_many_fields(observed_file)
        expected = read_many_fields(expected_file)
        self.assertEqual(observed, expected)
        remove_file(observed_file)

    def test_get_exon_junctions2(self):
        input_file = "{0}/tests/data/input_coding_exons.bed".format(MODULE_DIR)
        input_all_file = "{0}/tests/data/input_all_exons.bed".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_get_exon_junctions2.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_get_exon_junctions2.bed".format(MODULE_DIR)
        remove_file(observed_file)
        get_exon_junctions(input_file, observed_file, all_exons_file = input_all_file)
        observed = read_many_fields(observed_file)
        expected = read_many_fields(expected_file)
        self.assertEqual(observed, expected)
        # remove_file(observed_file)
