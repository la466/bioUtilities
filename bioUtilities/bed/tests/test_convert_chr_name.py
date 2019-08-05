from bioUtilities.bed import MODULE_DIR, convert_chr_name
from bioUtilities.files import remove_file, read_many_fields
import unittest

class TestConvertChrName(unittest.TestCase):

    def test_convert_chr_name1(self):
        input_bed = "{0}/tests/data/input.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_convert_chr_name1.bed".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_convert_chr_name1.bed".format(MODULE_DIR)
        remove_file(observed_file)
        convert_chr_name(input_bed, observed_file)
        observed = read_many_fields(observed_file)
        expected = read_many_fields(expected_file)
        self.assertEqual(expected, observed)
        remove_file(observed_file)

    def test_convert_chr_name2(self):
        input_bed = "{0}/tests/data/input.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_convert_chr_name1.bed".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_convert_chr_name1.bed".format(MODULE_DIR)
        remove_file(observed_file)
        convert_chr_name(input_bed, observed_file)
        observed = read_many_fields(observed_file)
        expected = read_many_fields(expected_file)
        self.assertEqual(expected, observed)
        remove_file(observed_file)
