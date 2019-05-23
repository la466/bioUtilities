import csv

def read_many_fields(input_file, delimiter):
    """
    Read a csv/tsv/... into a list of lists with each sublist corresponding to one line.

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
    >>> from utilities.file_ops import read_many_fields
    >>> read_many_fields("test_file.csv", ",")
    [[entry1, entry2, entry3],[entry4, entry5, entry6]]
    """

    file_to_read = open(input_file)
    # default to tab if no delimiter is given
    if not delimiter:
        delimiter = "\t"
    try:
        field_reader = csv.reader(file_to_read, delimiter = delimiter)
        lines = []
        for i in field_reader:
            lines.append(i)
        file_to_read.close()
        return(lines)
    except:
        print("Problem reading file...")
        return [["Problem reading file"]]
