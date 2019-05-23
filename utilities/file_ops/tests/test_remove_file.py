from utilities.file_ops import MODULE_DIR, remove_file
import unittest
import os

class TestRemoveFile(unittest.TestCase):

    def test_remove_file(self):
        filepath = "{0}/tests/data/test_remove_file.txt".format(MODULE_DIR)
        # write to a test file
        with open(filepath, "w") as file:
            pass
        # remove the file
        remove_file(filepath)
        self.assertFalse(os.path.isfile(filepath))
