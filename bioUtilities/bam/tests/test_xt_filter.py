from bioUtilities.bam import MODULE_DIR, xt_filter
from bioUtilities.commands import run_process
from bioUtilities.files import remove_file, read_many_fields
import unittest
import os

class TestXTFilter(unittest.TestCase):

    def test_xt_filter(self):
        input_file = "{0}/tests/data/input.bam".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_xt_filter.sam".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_xt_filter.bam".format(MODULE_DIR)
        xt_filter(input_file, observed_file, filter = "XT:A:U")
        #convert bam to sam to check correct output
        temp_observed = "{0}/tests/data/observed_xt_filter.sam".format(MODULE_DIR)
        samtools_args = ["samtools", "view", observed_file]
        run_process(samtools_args, file_for_output = temp_observed)
        expected = read_many_fields(expected_file, "\t")
        observed = read_many_fields(temp_observed, "\t")
        self.assertEqual(expected, observed)
        remove_file(temp_observed)
        remove_file(observed_file)
