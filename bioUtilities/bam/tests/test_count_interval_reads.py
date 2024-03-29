from bioUtilities.bam import MODULE_DIR, count_interval_reads
from bioUtilities.files import remove_file, read_many_fields
import unittest

class TestCountIntervalReads(unittest.TestCase):

    def test_read_count(self):
        input_bed = "{0}/tests/data/input2.bed".format(MODULE_DIR)
        input_bam = "{0}/tests/data/input2.bam".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_count_interval_reads.saf".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_count_interval_reads.saf".format(MODULE_DIR)
        remove_file(observed_file)
        count_interval_reads(input_bed, input_bam, observed_file)
        observed = read_many_fields(observed_file)[2:]
        expected = read_many_fields(expected_file)
        self.assertEqual(observed, expected)
        remove_file(observed_file)
        remove_file("{0}.summary".format(observed_file))

    def test_read_count_bed(self):
        input_bed = "{0}/tests/data/input2.bed".format(MODULE_DIR)
        input_bam = "{0}/tests/data/input2.bam".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_count_interval_reads.bed".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_count_interval_reads.bed".format(MODULE_DIR)
        remove_file(observed_file)
        count_interval_reads(input_bed, input_bam, observed_file)
        observed = read_many_fields(observed_file)
        expected = read_many_fields(expected_file)
        self.assertEqual(observed, expected)
        remove_file(observed_file)
        remove_file("{0}.saf.summary".format(observed_file[:-4]))
