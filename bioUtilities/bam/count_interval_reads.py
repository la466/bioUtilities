import os
import shutil

from bioUtilities.bed import bed_to_saf
from bioUtilities.commands import run_process
from bioUtilities.files import remove_file, read_many_fields, get_extension

def count_interval_reads(input_file, input_bam, output_file, paired_end = False, min_qual = None, min_length = 50):
    """
    For each interval in bed format, count the number of reads in the bam file

    Parameters
    ---------
    input_file : str
        Path to the file containing the intervals
    input_bam : str
        Path to the .bam file containing the reads
    output_file : str
        Path to the output file


    Dependencies
    ---------
    featureCounts v1.6.4

    Examples
    ---------
    >>> from bioUtilities.bam import count_interval_reads
    >>> count_interval_reads("exon_junctions.bed", "reads.bam", "exon_junction_reads.bed")
    """

    # check that featureCounts command exists
    if not shutil.which('featureCounts'):
        raise Exception('\nERROR: featureCounts must be installed.\n')

    # if input_file is in bed format, need to convert to .saf format
    # .saf format its 1-based
    if get_extension(input_file) == ".bed":
        base_input_file = input_file
        working_input_file = "{0}.saf".format(input_file[:-4])
        bed_to_saf(old_input_file, input_file)
    else:
        working_input_file = input_file

    if get_extension(output_file) == ".bed":
        working_output_file = "{0}.saf".format(output_file[:-4])
    else:
        working_output_file = output_file

    # now can use featureCounts to count reads
    # this return the file in 'saf' format
    args = ["featureCounts", "-fO", "-F", "SAF", "-g", "ID"]
    if paired_end:
        args.append("-p")
    if min_qual:
        args.extend(["-Q", min_qual])
    if min_length:
        args.extend(["-d", min_length])
    args.extend(["-a", working_input_file, "-o", working_output_file, input_bam])

    # now run the count
    run_process(args)

    # if the output format is bed, convert the saf output to bed
    if get_extension(output_file) == ".bed":
        entries = read_many_fields(working_output_file)[2:]
        with open(output_file, "w") as outfile:
            for entry in entries:
                output = [entry[1], str(int(entry[2])-1), str(int(entry[3])-1), entry[0], ".", entry[4]]
                output.extend(entry[5:])
                outfile.write("{0}\n".format("\t".join(output)))

    # now clean up the files
    if working_input_file != input_file:
        remove_file(working_input_file)
    if working_output_file != output_file:
        remove_file(output_file)
