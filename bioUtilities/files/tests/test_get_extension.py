from bioUtilities.files import MODULE_DIR, get_extension
import unittest
import os

class TestGetExtension(unittest.TestCase):

    def test_get_extension_txt(self):
        filepath = "{0}/tests/data/test_file_comma_delimited.txt".format(MODULE_DIR)
        expected = ".txt"
        observed = get_extension(filepath)
        self.assertEqual(expected, observed)

    def test_get_extension_bed(self):
        filepath = "{0}/tests/data/test_file_tab_delimited.bed".format(MODULE_DIR)
        expected = ".bed"
        observed = get_extension(filepath)
        self.assertEqual(expected, observed)

    def test_get_extension_fail(self):
        filepath = "{0}/tests/data/test_file_tab_delimited.txt".format(MODULE_DIR)
        self.assertRaises(AttributeError, get_extension, [filepath, [".jpg", ".bed"]])
