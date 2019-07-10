from bioUtilities.files import read_many_fields

def convert_zero_to_one(input_file, output_file, delimiter = "\t"):
    """
    Given a bed file in index 0 format, convert entries to index 1 format

    Parameters
    ---------
    input_file : str
        Path to the file to convert
    output_file : str
        Path to the output file
    delimiter : str
        If set, the delimiter for the bed file

    Examples
    ---------
    >>> from bioUtilities.bed import convert_zero_to_one
    >>> convert_zero_to_one("exon_junctions.bed", "exon_junction_index_1.bed")
    """

    entries = read_many_fields(input_file, delimiter)
    with open(output_file, "w") as outfile:
        for entry in entries:
            entry[1] = str(int(entry[1]) + 1)
            entry[2] = str(int(entry[2]) + 1)
            outfile.write("{0}\n".format(delimiter.join(entry)))
