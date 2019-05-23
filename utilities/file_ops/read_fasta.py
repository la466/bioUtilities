from collections import namedtuple

FastaEntries = namedtuple('FastaEntries', ('names', 'sequences'))

def read_fasta(input_file):
    """
    Read a .fa/.fasta file, returning

    Parameters
    ---------
        input_file : str
            path to the file that is to be read
        delimiter : str, optional
            delimiter of the file

    Returns
    ---------
        lines : list
            list of lines containing the entries separated by the delimiter
            specified

    Examples
    ---------
    >>> from file_ops import read_many_fields
    >>> read_many_fields("test_file.csv", ",")
    [[entry1, entry2, entry3],[entry4, entry5, entry6]]
    """

    file_to_read = open(input_file)
    input_lines = file_to_read.readlines()
    file_to_read.close()
    input_lines = [i.rstrip("\n") for i in input_lines]
    names = [i.lstrip(">") for i in input_lines if i[0] == ">"]
    sequences = [i for i in input_lines if i[0] != ">"]
    if len(sequences) != len(names):
        print("Problem extracting data from fasta file!")
        print(len(sequences))
        print(len(names))
        raise Exception
    if len(sequences) == 0:
        print("No sequences were extracted!")
        raise Exception
    return(names, sequences)
