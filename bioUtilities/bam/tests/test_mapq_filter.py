from bioUtilities.bam import MODULE_DIR, mapq_filter
from bioUtilities.commands import run_process
from bioUtilities.files import remove_file, read_many_fields
import unittest
import os

class TestMAPQFilter(unittest.TestCase):

    def test_mapq_filter_lower_limit(self):
        input_file = "{0}/tests/data/input.bam".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_mapq_filter_1.sam".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_mapq_filter_1.bam".format(MODULE_DIR)
        mapq_filter(input_file, observed_file, lower_limit = 200)
        expected = read_many_fields(expected_file, "\t")
        # convert bam to sam to check correct output
        # use samtools to extract in the same format as sam
        temp_observed = "{0}/tests/data/observed_mapq_filter_1.sam".format(MODULE_DIR)
        samtools_args = ["samtools", "view", observed_file]
        run_process(samtools_args, file_for_output = temp_observed)
        observed = read_many_fields(temp_observed, "\t")
        self.assertEqual(expected, observed)
        remove_file(temp_observed)
        remove_file(observed_file)

    def test_mapq_filter_upper_limit(self):
        input_file = "{0}/tests/data/input.bam".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_mapq_filter_2.sam".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_mapq_filter_2.bam".format(MODULE_DIR)
        mapq_filter(input_file, observed_file, upper_limit = 200)
        expected = read_many_fields(expected_file, "\t")
        # convert bam to sam to check correct output
        # use samtools to extract in the same format as sam
        temp_observed = "{0}/tests/data/observed_mapq_filter_2.sam".format(MODULE_DIR)
        samtools_args = ["samtools", "view", observed_file]
        run_process(samtools_args, file_for_output = temp_observed)
        observed = read_many_fields(temp_observed, "\t")
        self.assertEqual(expected, observed)
        remove_file(temp_observed)
        remove_file(observed_file)

    def test_mapq_filter_both_limits(self):
        input_file = "{0}/tests/data/input.bam".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_mapq_filter_3.sam".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_mapq_filter_3.bam".format(MODULE_DIR)
        mapq_filter(input_file, observed_file, lower_limit = 100, upper_limit = 200)
        expected = read_many_fields(expected_file, "\t")
        # convert bam to sam to check correct output
        # use samtools to extract in the same format as sam
        temp_observed = "{0}/tests/data/observed_mapq_filter_3.sam".format(MODULE_DIR)
        samtools_args = ["samtools", "view", observed_file]
        run_process(samtools_args, file_for_output = temp_observed)
        observed = read_many_fields(temp_observed, "\t")
        self.assertEqual(expected, observed)
        remove_file(temp_observed)
        remove_file(observed_file)
