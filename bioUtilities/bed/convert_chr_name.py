from bioUtilities.files import read_many_fields

def convert_chr_name(input_file, output_file,  full_name = False, delimiter = "\t"):
    """
    Given a bed file, convert the chromosome name for use between formats

    Parameters
    ---------
    input_file : str
        Path to the file to convert
    output_file : str
        Path to the output file
    header : bool
        If true, header present and ignore
    delimiter : str
        If set, the delimiter for the bed file

    Examples
    ---------
    >>> from bioUtilities.bed import convert_chr_name
    >>> convert_chr_name("input.bed", "input_converted.bed")
    >>> convert_chr_name("input1.bed", "input_converted1.bed", full_name = True)
    """

    entries = read_many_fields(input_file, delimiter = delimiter)

    with open(output_file, "w") as outfile:
        for entry in entries:
            if full_name:
                entry[0] = "chr{0}".format(entry[0])
            else:
                entry[0] = entry[0].strip("chr")
            outfile.write("{0}\n".format("\t".join(entry)))
