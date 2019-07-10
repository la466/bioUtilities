from bioUtilities.bed import MODULE_DIR, get_terminal_coordinates
from bioUtilities.files import remove_file, read_many_fields
import unittest

class TestGetTerminalCoordinates(unittest.TestCase):

    def test_get_terminal_coordinates(self):
        input_bed = "{0}/tests/data/input2.bed".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_get_terminal_coordinates.bed".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_get_terminal_coordinates.bed".format(MODULE_DIR)
        remove_file(observed_file)
        get_terminal_coordinates(input_bed, observed_file)
        observed = read_many_fields(observed_file)
        expected = read_many_fields(expected_file)
        self.assertEqual(expected, observed)
        remove_file(observed_file)
