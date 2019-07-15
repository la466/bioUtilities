from bioUtilities.bed import MODULE_DIR, bed_to_saf
from bioUtilities.files import remove_file, read_many_fields
import unittest

class TestBedToSaf(unittest.TestCase):

    def test_bed_to_saf(self):
        input_bed = "{0}/tests/data/input.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_bed_to_saf.saf".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_bed_to_saf.saf".format(MODULE_DIR)
        remove_file(observed_file)
        bed_to_saf(input_bed, observed_file)
        observed = read_many_fields(observed_file)
        expected = read_many_fields(expected_file)
        self.assertEqual(expected, observed)
        remove_file(observed_file)
