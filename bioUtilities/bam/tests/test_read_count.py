from bioUtilities.bam import MODULE_DIR, read_count
import unittest

class TestReadCount(unittest.TestCase):

    def test_read_count(self):
        input_file = "{0}/tests/data/input.bam".format(MODULE_DIR)
        expected = 22
        observed = read_count(input_file)
        self.assertEqual(expected, observed)
