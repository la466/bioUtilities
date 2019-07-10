from bioUtilities.bam import MODULE_DIR, intersect_with_bed
from bioUtilities.files import remove_file, read_many_fields
from bioUtilities.commands import run_process
import unittest

class TestIntersectWithBed(unittest.TestCase):

    def test_intersect_with_bed(self):
        input_bed = "{0}/tests/data/input.bed".format(MODULE_DIR)
        input_bam = "{0}/tests/data/input3.bam".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_intersect_with_bed.bam".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_intersect_with_bed.sam".format(MODULE_DIR)
        remove_file(observed_file)
        intersect_with_bed(input_bam, input_bed, observed_file)
        observed_sam = "{0}/tests/data/observed_intersect_with_bed.sam".format(MODULE_DIR)
        args = ["samtools", "view", "-h", observed_file]
        run_process(args, file_for_output = observed_sam)
        observed = read_many_fields(observed_sam)
        expected = read_many_fields(expected_file)
        self.assertEqual(expected, observed)
        remove_file(observed_file)
        remove_file(observed_sam)
