from bioUtilities.files import read_many_fields

def get_terminal_coordinates(input_file, output_file, delimiter = "\t"):
    """
    Given a bed file of sequence coordinates, return both the 5' and 3' terminal
    coordinates

    Parameters
    ---------
    input_file : str
        Path to the file to gett the coordinates for
    output_file : str
        Path to the output file
    delimiter : str
        If set, the delimiter for the bed file

    Examples
    ---------
    >>> from bioUtilities.bed import convert_zero_to_one
    >>> get_terminal_coordinates("exons.bed", "exon_terminal_nucleotides.bed")
    """

    entries = read_many_fields(input_file, delimiter)

    with open(output_file, "w") as outfile:
        for entry in entries:
            id = entry[3]
            start = int(entry[1])
            end = int(entry[2])
            five_prime_entry = [entry[0], str(start), str(start + 1), "{0}.5".format(id)] + entry[4:]
            three_prime_entry = [entry[0], str(end - 1), str(end), "{0}.3".format(id)] + entry[4:]
            outfile.write("{0}\n".format(delimiter.join(five_prime_entry)))
            outfile.write("{0}\n".format(delimiter.join(three_prime_entry)))
