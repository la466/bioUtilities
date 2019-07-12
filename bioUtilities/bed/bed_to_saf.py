from bioUtilities.files import read_many_fields

def bed_to_saf(input_file, output_file, header = False, delimiter = "\t"):
    """
    Given a bed file, convert to saf format
    See http://bioinf.wehi.edu.au/featureCounts/

    Parameters
    ---------
    input_file : str
        Path to the file to convert
    output_file : str
        Path to the output file
    header : bool
        If true, header present nad ignore
    delimiter : str
        If set, the delimiter for the bed file

    Examples
    ---------
    >>> from bioUtilities.bed import bed_to_saf
    >>> bed_to_saf("input.bed", "output.saf")
    """

    entries = read_many_fields(input_file, delimiter = delimiter)
    # if header exists, ignore it
    if header:
        entries = entries[1:]

    with open(output_file, "w") as outfile:
        header = ["ID", "Chr", "Start", "End", "Strand"]
        if len(entries[0]) > 5:
            header.append("Info")
        outfile.write("{0}\n".format("\t".join(header)))
        for entry in entries:
            output = [entry[3], entry[0], entry[1], entry[2], entry[5]]
            if len(entry) > 5:
                output.append(",".join(entry[6:]))
            outfile.write("{0}\n".format("\t".join(output)))
