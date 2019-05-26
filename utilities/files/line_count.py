from utilities.commands import run_process
import re

def line_count(filepath):
    """
    Count the number of lines in a file

    Parameters
    ---------
    filepath : str
        Path to the file

    Returns
    ---------
    line_count : int
        The number of lines in the file

    Examples
    ---------
    >>> from utilities.file_ops import line_count
    >>> line_count("test_file.txt")
    3
    """

    count_output = run_process(["wc", "-l", filepath])
    line_count = int(re.findall("\s+(\d+)", count_output)[0])
    return line_count
