import os
import random

from bioUtilities.commands import run_process
import bioUtilities.files

def fasta_from_bed(bed_file, genome_fasta, output_file, force_strand = True, names = False, write_strand = False):
    """
    Takes a bed file and creates a fasta file with the corresponding sequences.

    Parameters
    ---------
    bed_file : str
        Path to the bed file
    genome_fasta : str
        Path to genome fasta file
    output_file : str
        Path to output file
    force_strand : bool
        If set, force strandedness. If the feature occupies the antisense strand,
        the sequence will be reverse complemented
    names : bool
        If set, use the “name” column in the bed file for the headers in the
        output file.
    write_strand : bool
        If true, keep the strand info

    Examples
    ---------
    >>> from bioUtilities.files import fasta_from_bed
    >>> fasta_from_bed("path_to_bed.bed", "path_to_genome.fa", "output.fa", force_strand = True, names = True)

    Dependencies
    ---------
    bedtools
    """

    # check whether the index file exists, if not generate the file
    genome_fasta_index = "{0}.fai".format(genome_fasta)
    if not os.path.exists(genome_fasta_index):
        run_process(["samtools", "faidx", genome_fasta])

    # check whether the bed file chrs are in the genome fasta
    bed_chrs = sorted(list(set([entry[0] for entry in bioUtilities.files.read_many_fields(bed_file)])))
    index_chrs = sorted(list(set([entry[0] for entry in bioUtilities.files.read_many_fields(genome_fasta_index)])))
    if not set(bed_chrs).issubset(set(index_chrs)):
        raise Exception("\nERROR: bed file chr are not found in genome fasta\n")

    # run bedtools
    temp_file = "temp.{0}.fa".format(random.random())
    args = ["bedtools", "getfasta", "-s", "-fi", genome_fasta, "-bed", bed_file, "-fo", temp_file]
    if not force_strand:
        del args[2]
    if names:
        args.append("-name")
    run_process(args)

    entries = bioUtilities.files.read_fasta(temp_file)
    ids = [i.split("(")[0] if names and not write_strand else i for i in entries.ids]
    sequences = [i.upper() for i in entries.sequences]
    # write the entries to output file
    bioUtilities.files.write_fasta({id: sequences[i] for i, id in enumerate(ids)}, output_file)
    # remove the temp file
    bioUtilities.files.remove_file(temp_file)
