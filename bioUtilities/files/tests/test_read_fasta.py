from bioUtilities.files import MODULE_DIR, read_fasta
from bioUtilities.tests import common_tests
import unittest
import os

class TestReadFasta(unittest.TestCase):

    def test_read_fasta(self):
        filepath = "{0}/tests/data/test_file_fasta.fa".format(MODULE_DIR)
        observed = read_fasta(filepath)
        common_tests.check_named_results(observed, [["id1", "id2"], ["AAGCTACAG", "AGCATCAG"]], ["ids", "sequences"])

    def test_read_fasta_empty(self):
        filepath = "{0}/tests/data/test_file_fasta_empty.fa".format(MODULE_DIR)
        self.assertRaises(Exception, read_fasta, filepath)

    def test_read_fasta_problem(self):
        filepath = "{0}/tests/data/test_file_fasta_problem.fa".format(MODULE_DIR)
        self.assertRaises(Exception, read_fasta, filepath)
