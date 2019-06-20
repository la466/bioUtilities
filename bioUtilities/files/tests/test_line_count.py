from bioUtilities.files import MODULE_DIR, line_count
import unittest
import os

class TestLineCount(unittest.TestCase):

    def test_line_count(self):
        filepath = "{0}/tests/data/test_file_fasta.fa".format(MODULE_DIR)
        observed = line_count(filepath)
        self.assertEqual(observed, 4)

    def test_line_count_empty(self):
        filepath = "{0}/tests/data/test_file_fasta_empty.fa".format(MODULE_DIR)
        observed = line_count(filepath)
        self.assertEqual(observed, 0)
