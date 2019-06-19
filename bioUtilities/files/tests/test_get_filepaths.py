from bioUtilities.file_ops import MODULE_DIR, get_filepaths
import unittest
import os

class TestGetFilePaths(unittest.TestCase):

    def test_get_filepaths(self):
        directory = "{0}/tests/data/test_dir".format(MODULE_DIR)
        observed = get_filepaths(directory)
        expected = ["{0}/test_file1.txt".format(directory), "{0}/test_file2.txt".format(directory)]
        self.assertEqual(observed, expected)

    def test_get_filepaths_with_hidden(self):
        directory = "{0}/tests/data/test_dir".format(MODULE_DIR)
        observed = get_filepaths(directory, return_hidden = True)
        expected = ["{0}/.test_hidden.txt".format(directory), "{0}/test_file1.txt".format(directory), "{0}/test_file2.txt".format(directory)]
        self.assertEqual(observed, expected)
