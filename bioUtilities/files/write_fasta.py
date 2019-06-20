def write_fasta(input_dict, output_file):
    """
    Given a dictionary, write to an output file

    Parameters
    ---------
    input_dict : dict
        Dictionary containing ids and items to be written
    output_file : str
        Path to the output file

    Examples
    ---------
    >>> from bioUtilities.files import write_fasta
    >>> to_write = {"id1": "ATCACG", "id2": "ACATTGF"}
    >>> write_fasta(to_write, "output_file.fa")
    """

    with open(output_file, "w") as outfile:
        [outfile.write(">{0}\n{1}\n".format(i, input_dict[i])) for i in input_dict]
