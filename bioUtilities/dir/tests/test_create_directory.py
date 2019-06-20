from bioUtilities.dir import MODULE_DIR, create_directory
import unittest
import os
import shutil

class TestCreateDirectory(unittest.TestCase):

    def test_create_directory(self):
        dir = "test_directory/level2"
        create_directory(dir)
        self.assertTrue(os.path.exists(dir))
        shutil.rmtree("test_directory")
