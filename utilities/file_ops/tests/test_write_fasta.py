from utilities.file_ops import MODULE_DIR, remove_file, read_fasta, write_fasta
from utilities.tests import common_tests
import unittest
import os

class TestRemoveFile(unittest.TestCase):

    def test_write_fasta(self):
        filepath = "{0}/tests/data/test_write_fasta.fa".format(MODULE_DIR)
        remove_file(filepath)
        input_dict = {"id1": "TACGAGAT", "id2": "ATCGAGCGCGC"}
        write_fasta(input_dict, filepath)
        common_tests.check_named_results(read_fasta(filepath), [["id1", "id2"], ["TACGAGAT", "ATCGAGCGCGC"]], ["ids", "sequences"])
