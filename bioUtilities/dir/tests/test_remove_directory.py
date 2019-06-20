from bioUtilities.dir import MODULE_DIR, remove_directory
import unittest
import os
import shutil

class TestRemoveDirectory(unittest.TestCase):

    def test_create_directory(self):
        dir = "test_directory"
        os.makedirs(dir, exist_ok=True)
        remove_directory(dir)
        self.assertFalse(os.path.exists(dir))
