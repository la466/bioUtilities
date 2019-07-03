from bioUtilities.files import MODULE_DIR, parse_gtf, read_many_fields, remove_file
import unittest
import os

class TestParseGTF(unittest.TestCase):

    def test_parse_gtf1(self):
        input_file = "{0}/tests/data/input.gtf".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_parse_gtf1.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_parse_gtf1.bed".format(MODULE_DIR)
        parse_gtf(input_file, features = ["exon"], protein_coding = True, output_file = observed_file)
        expected = read_many_fields(expected_file, "\t")
        observed = read_many_fields(observed_file, "\t")
        self.assertEqual(observed, expected)
        remove_file(observed_file)

    def test_parse_gtf2(self):
        input_file = "{0}/tests/data/input.gtf".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_parse_gtf2.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_parse_gtf2.bed".format(MODULE_DIR)
        parse_gtf(input_file, features = ["exon"], transcript_ids = ["ENST00000456328"], output_file = observed_file)
        expected = read_many_fields(expected_file, "\t")
        observed = read_many_fields(observed_file, "\t")
        self.assertEqual(observed, expected)
        remove_file(observed_file)
