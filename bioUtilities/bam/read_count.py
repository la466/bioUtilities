import re

from bioUtilities.commands import run_process

def read_count(input_file):
    """
    Get the number of reads from a .bam/.sam file

    Parameters
    ---------
    input_file : str
        Path to the file to be counted

    Returns
    ---------
    read_count : int
        The number of reads in the specified file

    Examples
    ---------
    >>> from bioUtilities.bam import read_count
    >>> reads = read_count("test.bam")
    >>> print(reads)
    >>> 15
    """

    raw_read_count = run_process(["samtools", "view", "-c", input_file])
    read_count = int(re.findall("(\d+)", raw_read_count)[0])
    return read_count
