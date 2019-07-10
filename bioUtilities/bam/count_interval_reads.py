import os

from bioUtilities.commands import run_process

def count_interval_reads(input_bed, input_bam, output_file, force_strand = False, index_file = True):
    """
    For each interval in bed format, count the number of reads in the bam file

    Parameters
    ---------
    input_bed : str
        Path to the .bed file containing the intervals
    input_bam : str
        Path to the .bam file containing the reads
    output_file : str
        Path to the output file
    force_strand : bool
        If set, force reads to match strand in bed file
    index_file : bool
        If set, create the index file

    Examples
    ---------
    >>> from bioUtilities.bam import count_interval_reads
    >>> count_interval_reads("exon_junctions.bed", "reads.bam", "exon_junction_reads.bed")
    """

    # need to index the .bam file if it doesnt already exist
    if not os.path.exists("{0}.bai".format(input_bam)) or not index_file:
        index_args = ["samtools", "index", input_bam]
        run_process(index_args)

    # now use bedtools to count the reads
    args = ["bedtools", "multicov", "-s", "-D", "-F", "-bams", input_bam, "-bed", input_bed]
    if not force_strand:
        del args[2]
    run_process(args, file_for_output = output_file)
