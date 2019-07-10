from bioUtilities.bed import MODULE_DIR, convert_one_to_zero
from bioUtilities.files import remove_file, read_many_fields
import unittest

class TestConvertOneToZero(unittest.TestCase):

    def test_convert_one_to_zero(self):
        input_bed = "{0}/tests/data/input.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_convert_one_to_zero.bed".format(MODULE_DIR)
        expected_file = "{0}/tests/data/observed_convert_one_to_zero.bed".format(MODULE_DIR)
        remove_file(observed_file)
        convert_one_to_zero(input_bed, observed_file)
        observed = read_many_fields(observed_file)
        expected = read_many_fields(expected_file)
        self.assertEqual(expected, observed)
        remove_file(observed_file)
