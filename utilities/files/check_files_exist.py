import os
from collections import namedtuple

FilesExist = namedtuple('FilesExist', ('exist', 'missing'))

def check_files_exist(filepath_list):
    """
    Check whether a given list of files exist

    Parameters
    ---------
        filepath_list : list
            List of files to check paths of

    Returns
    ---------
        exist : bool
            True is all files exist
        missing_files : list
            A list of missing files

    Examples
    ---------
    >>> from utilities.file_ops import check_files_exist
    >>> check_files_exist(["test_fasta.fa"])
    FilesExist(exists=True, missing=[]])
    >>> check_files_exist(["test_fasta.fa", "test.txt"])
    FilesExist(exists=False, missing=["test.txt"]])
    """

    missing = []

    for filepath in filepath_list:
        if not os.path.isfile(filepath):
            missing.append(filepath)

    if len(missing) != 0:
        return FilesExist(False, missing)
    else:
        return FilesExist(True, [])
