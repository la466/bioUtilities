import os

from bioUtilities.commands import run_process

def intersect_with_bed(input_bam, input_bed, output_file, force_strand = True):
    """
    Given a bam file, intersect with a bed file to leave only thse reads that
    correspond to entries in the bed file

    Parameters
    ---------
    input_bam : str
        Path to the .bam file containing the reads
    input_bed : str
        Path to the .bed file containing the intervals
    output_file : str
        Path to the output file
    force_strand : bool
        If set, ensure the reads map to the same strand

    Examples
    ---------
    >>> from bioUtilities.bam import intersect_with_bed
    >>> intersect_with_bed("reads.bam", "exons.bed", "exon_reads.bam")
    """

    # now use bedtools to count the reads
    args = ["bedtools", "intersect", "-s", "-abam", input_bam, "-b", input_bed]
    print(" ".join(args))
    if not force_strand:
        del args[2]
    run_process(args, file_for_output = output_file)
