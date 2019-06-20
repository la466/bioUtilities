import os

def get_filepaths(directory, return_hidden = False):
    """
    Return the filepaths in the given directory

    Parameters
    ---------
    directory : str
        Path to the directory in question
    return_hidden : bool
        If True, return hidden files too

    Returns
    ---------
    filepaths : list
        The paths of all files in the directory

    Examples
    ---------
    >>> from bioUtilities.files import get_filepaths
    >>> get_filepaths("./tests/test_directory")
    ['tests/test_directory/file1.txt', 'tests/test_directory/file2.txt']
    """

    filepaths = []
    for file in os.listdir(directory):
        filepath = "{0}/{1}".format(directory, file)
        if return_hidden:
            filepaths.append(filepath)
        else:
            if not file.startswith("."):
                filepaths.append(filepath)
    return filepaths
