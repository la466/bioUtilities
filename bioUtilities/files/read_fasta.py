from collections import namedtuple

FastaEntries = namedtuple('FastaEntries', ('ids', 'sequences'))

def read_fasta(input_file):
    """
    Read a .fa/.fasta file, returning the ids and sequences for each entry

    Parameters
    ---------
    input_file : str
        Path to the file that is to be read

    Returns
    ---------
    names : list
        The list of fasta entry ids
    sequences : list
        The list of fasta entry sequences

    Examples
    ---------
    >>> from bioUtilities.files import read_fasta
    >>> read_fasta("test_fasta.fa")
    FastaEntries(ids=['id1', 'id2'], sequences=['AAGCTACAG', 'AGCATCAG'])
    """

    file_to_read = open(input_file)
    input_lines = file_to_read.readlines()
    file_to_read.close()
    input_lines = [i.rstrip("\n") for i in input_lines]
    ids = [i.lstrip(">") for i in input_lines if i[0] == ">"]
    sequences = [i for i in input_lines if i[0] != ">"]
    if len(sequences) != len(ids):
        raise Exception("\n\nERROR: Problem extracting sequences.\n{0} ids\n{1} sequences\n".format(len(ids), len(sequences)))
    if len(sequences) == 0:
        raise Exception("\n\nERROR: No sequences could be extracted.\n")
    return FastaEntries(ids, sequences)
