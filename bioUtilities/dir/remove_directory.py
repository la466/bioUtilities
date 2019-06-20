import shutil
import os

def remove_directory(path):
    """
    Check if directory exists and if so, delete.

    Parameters
    ---------
    path : str
        Path of the directory to remove

    Examples
    ---------
    >>> from bioUtilities.dir import remove_directory
    >>> remove_directory("test_directory/another_directory")
    """

    if os.path.exists(path):
        shutil.rmtree(path)
