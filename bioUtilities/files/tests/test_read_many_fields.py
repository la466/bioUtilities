from bioUtilities.files import MODULE_DIR, read_many_fields
import unittest
import os

class TestReadManyFields(unittest.TestCase):

    def test_read_many_fields_comma(self):
        filepath = "{0}/tests/data/test_file_comma_delimited.txt".format(MODULE_DIR)
        expected = [["entry1.1", "entry1.2", "entry1.3"], ["entry2.1", "entry2.2", "entry2.3"]]
        observed = read_many_fields(filepath, ",")
        self.assertEqual(expected, observed)

    def test_read_many_fields_tab(self):
        filepath = "{0}/tests/data/test_file_tab_delimited.bed".format(MODULE_DIR)
        expected = [["entry1.1", "entry1.2", "entry1.3"], ["entry2.1", "entry2.2", "entry2.3"]]
        observed = read_many_fields(filepath, "\t")
        self.assertEqual(expected, observed)
