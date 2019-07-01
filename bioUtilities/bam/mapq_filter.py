from bioUtilities.commands import run_process
from bioUtilities.files import remove_file
from bioUtilities.dir import create_directory, remove_directory
import random

def mapq_filter(input_file, output_file, lower_limit = None, upper_limit = None):
    """
    Filter a .bam/.sam by MAPQ value

    Parameters
    ---------
    input_file : str
        Path to the file to be filtered
    output_file : str
        Path to the output
    lower_limit : int
        If set, the lower boundary of mapq values, for which all reads have to
        be greater than or equal to
    upper_limit : int
        If set, the upper boundary of mapq values, for which all reads have to
        be less than or equal to

    Examples
    ---------
    >>> from bioUtilities.bam import xt_filter
    >>> mapq_filter("test.bam", "test_output.bam", lower_limit = 100)
    >>> mapq_filter("test.bam", "test_output.bam", upper_limit = 250)
    >>> mapq_filter("test.bam", "test_output.bam", lower_limit = 100, upper_limit = 250)
    """

    #if neither thresholds are specified
    if not lower_limit and not upper_limit:
        raise Exception("You must specify at least one of the lower_limit or upper_limit thresholds")

    samtools_args = ["samtools", "view", "-h"]
    # if both thresholds are specified, we want the reads with values between these
    if lower_limit and upper_limit:
        # create temp file
        temp_directory = "temp_mapq_filter.{0}".format(random.random())
        create_directory(temp_directory)
        temp_file = "{0}/{1}".format(temp_directory, output_file.split("/")[-1])
        # first get everything above the lower limit
        temp_args = samtools_args.copy()
        temp_args.extend(["-q", lower_limit, input_file])
        run_process(temp_args, file_for_output = temp_file)
        # now get everything below the upper limit. need to account for
        # samtools removing everything below threshold
        # so when inversing need to add 1 to total
        temp_args = samtools_args.copy()
        upper_limit = upper_limit + 1
        temp_args.extend(["-q", upper_limit, temp_file, "-U", output_file])
        run_process(temp_args)
        # cleanup the temp files
        remove_directory(temp_directory)
    # if only a lower limit is specified
    elif lower_limit and not upper_limit:
        samtools_args.extend(["-bq", lower_limit, input_file])
        run_process(samtools_args, file_for_output = output_file)
    #if only the upper threshold is specified
    elif upper_limit and not lower_limit:
        # account for inverse by adding 1
        upper_limit = upper_limit + 1
        samtools_args.extend(["-q", upper_limit, input_file, "-U", output_file])
        run_process(samtools_args)
