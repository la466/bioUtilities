from bioUtilities.commands import run_process
from bioUtilities.files import remove_file

def xt_filter(input_file, output_file, filter = None):
    """
    Filter a .bam/.sam file by the XT tag

    Parameters
    ---------
    input_file : str
        Path to the file to be filtered
    output_file : str
        Path to the output
    filter : str
        Filter than reads should contain


    Examples
    ---------
    >>> from bioUtilities.bam import xt_filter
    >>> xt_filter("test.bam", "test_xt_filtered.bam", filter = "XT:A:U")
    """

    if not xt_filter:
        raise Exception('\nXT filter not specified.\n')
    # if the output format is .bam, temporarily create .sam output file
    if output_file[-4:] == ".bam":
        temp_output_file = "{0}.sam".format(output_file[:-4])
    else:
        temp_output_file = output_file

    # get the header of the file
    sam_output = run_process(["samtools", "view", "-h", input_file])
    grep_args = []
    # get header lines
    grep_args.append("^@")
    # get XT values matching the filter
    grep_args.append("\|\t{0}\t".format(filter))
    grep_args = "".join(grep_args)
    # run the filter
    run_process(["grep", grep_args], input_to_pipe = sam_output, file_for_output = temp_output_file)

    # if wanting to create bam, create bam and delete sam
    if output_file != temp_output_file:
        samtools_args = ["samtools", "view", "-bh", temp_output_file]
        run_process(samtools_args, file_for_output = output_file)
        remove_file(temp_output_file)
