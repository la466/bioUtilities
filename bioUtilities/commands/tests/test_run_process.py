from bioUtilities.commands import MODULE_DIR, run_process
from bioUtilities.files import remove_file
import unittest
import os

class TestRemoveFile(unittest.TestCase):

    def test_run_process(self):
        filepath = "{0}/tests/data/test_file.txt".format(MODULE_DIR)
        remove_file(filepath)
        # simple test to create file
        args = ["touch", filepath]
        run_process(args)
        self.assertEqual(os.path.isfile(filepath), True)
