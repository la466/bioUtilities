def get_extension(path, valid_list = None):
    """
    Determine the extension at the end of a file name.
    valid_list: if supplied, the extension must be one of the ones specified in this list

    EX: get_extension("test.jpg", 3, valid_list = ["jpg", "gif", "png"]) would return "jpg"

    Parameters
    ---------
    path : str
        path to the file being queried
    valid_list : list, optional
        list of valid extensions

    Returns
    ---------
    extension : str
        the file extension

    Examples
    ---------
    >>> from bioUtilities.file_ops import get_extension
    >>> print(get_extension("test_file.csv"))
    .csv
    >>> print(get_extension("test_file.csv", valid_list = [".jpg", ".csv", ".txt"]))
    .csv
    >>> print(get_extension("test_file.png", valid_list = [".jpg", ".csv", ".txt"]))

    ERR: File format must be one of [".jpg", ".csv", ".txt"]

    """

    extension = "." + path.split(".")[-1]
    if valid_list and extension not in valid_list:
        raise AttributeError("\n\nERROR: File format must be one of: {0}\n".format(", ".join(valid_list)))
    return extension
