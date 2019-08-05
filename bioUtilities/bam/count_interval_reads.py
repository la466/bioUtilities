import os

from bioUtilities.bed import bed_to_saf
from bioUtilities.commands import run_process
from bioUtilities.files import remove_file, read_many_fields

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

    # need to convert to .saf format if in bed format
    # .saf format its 1-based
    if input_file[-4:] == ".bed":
        old_input_file = input_file
        input_file = "{0}.saf".format(input_file[:-4])
        bed_to_saf(old_input_file, input_file)

    if output_file[-4:] == ".bed":
        temp_output = "{0}.saf".format(output_file[:-4])
    else:
        temp_output = output_file

    # now can use featureCounts to count reads
    # this return the file in 'saf' format
    args = ["featureCounts", "-fO", "-F", "SAF", "-g", "ID"]
    if paired_end:
        args.append("-p")
    if min_qual:
        args.extend(["-Q", min_qual])
    if min_length:
        args.extend(["-d", min_length])
    args.extend(["-a", input_file, "-o", temp_output, input_bam])

    run_process(args)

    if output_file[-4:] == ".bed":
        entries = read_many_fields(temp_output)[2:]
        with open(output_file, "w") as outfile:
            for entry in entries:
                output = [entry[1], str(int(entry[2])-1), str(int(entry[3])-1), entry[0], ".", entry[4]]
                output.extend(entry[5:])
                outfile.write("{0}\n".format("\t".join(output)))

        remove_file(temp_output)

    if old_input_file[-4:] == ".bed":
        remove_file(input_file)
