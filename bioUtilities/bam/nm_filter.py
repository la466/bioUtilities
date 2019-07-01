from bioUtilities.commands import run_process
from bioUtilities.files import remove_file

def nm_filter(input_file, output_file, lower_limit = 0, upper_limit = 10):
    """
    Filter a .bam/.sam by NM value

    Parameters
    ---------
    input_file : str
        Path to the file to be filtered
    output_file : str
        Path to the output
    lower_limit : int
        If set, the lower boundary of NM values, for which all reads have to
        be greater than or equal to
    upper_limit : int
        If set, the upper boundary of NM values, for which all reads have to
        be less than or equal to

    Examples
    ---------
    >>> from bioUtilities.bam import nm_filter
    >>> nm_filter("test.bam", "test_output.bam", lower_limit = 2)
    >>> nm_filter("test.bam", "test_output.bam", upper_limit = 6)
    >>> nm_filter("test.bam", "test_output.bam", lower_limit = 2, upper_limit = 6)
    """

    # if neither thresholds are specified
    if not lower_limit and not upper_limit:
        raise Exception("\nERROR: You must specify at least one of the lower_limit or upper_limit thresholds.\n")

    if not lower_limit:
        print("Using the default lower limit of 0.")
    if not upper_limit:
        print("Using the default uppper limit of 10.")

    #create output file
    if output_file[-4:] == ".bam":
        temp_output_file = "{0}.sam".format(output_file[:-4])
    else:
        temp_output_file = output_file

    grep_args = ["^@"]
    for i in range(lower_limit, upper_limit + 1):
        grep_args.append("\|\tNM:i:{0}\t".format(i))
    grep_args = "".join(grep_args)

    # read in the file
    file_reads = run_process(["samtools", "view", "-h", input_file])
    # now run the grep args
    output = run_process(["grep", grep_args], input_to_pipe = file_reads, file_for_output = temp_output_file)

    # if the output file is in bam format
    if output_file != temp_output_file:
        samtools_args = ["samtools", "view", "-bh", temp_output_file]
        run_process(samtools_args, file_for_output = output_file)
        remove_file(temp_output_file)
