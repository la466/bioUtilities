from utilities.file_ops import MODULE_DIR, check_files_exist
from utilities.tests import common_tests
import unittest
import os

class TestRemoveFile(unittest.TestCase):

    def test_check_files_exist(self):
        filepath = "{0}/tests/data/test_file_fasta.fa".format(MODULE_DIR)
        common_tests.check_named_results(check_files_exist([filepath]), [True, []], ["exist", "missing"])

    def test_check_files_exist_file_missing(self):
        filepath1 = "{0}/tests/data/test_file_fasta.fa".format(MODULE_DIR)
        filepath2 = "{0}/tests/data/test_file_fasta1.fa".format(MODULE_DIR)
        common_tests.check_named_results(check_files_exist([filepath1, filepath2]), [False, [filepath2]], ["exist", "missing"])
