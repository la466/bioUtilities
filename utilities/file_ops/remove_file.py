import os

def remove_file(path):
    """
    If a file exists, remove it

    Parameters
    ---------
        path : str
            path to the file that is to be removed

    Examples
    ---------
    >>> from file_ops import read_many_fields
    >>> remove_file("test_file.txt")
    """

    try:
        os.remove(path)
    except FileNotFoundError:
        pass
