import bioUtilities.files
import re

def parse_gtf(input_file, features = [], protein_coding = None, gene_ids = None, transcript_ids = None, include_chrs = None, exclude_chrs = None, output_file = None):
    """
    Read a gtf file, returning the parts of the file specified.

    Parameters
    ---------
    input_file : str
        Path to the file that is to be read
    features : list
        List of features to extract from the gtf file
    protein_coding : bool
        If true, only retain if the entry contains protein coding
    gene_ids : list
        If set, retain only those entries with gene id in list
    transcript_ids : list
        If set, retain only those entries with transcript id in list
    include_chrs : list
        If set, a list of chromosomes to include
    exclude_chrs : list
        If set, a list of chromosomes to exclude
    output_file : str
        If set, write the features to an output file

    Returns
    ---------
    entries : list
        List of the entries that have been kept

    Examples
    ---------
    >>> from bioUtilities.files import parse_gtf
    >>> parse_gtf("test_gtf.gtf", features = ["exon"], protein_coding = True)
    """

    outputs = []
    # read the gtf file and remove meta data
    entries = [i for i in bioUtilities.files.read_many_fields(input_file, "\t") if "#" not in i[0]]
    # gene id search
    gene_id_regex = re.compile("gene_id\s\"([^\";]+)")
    # transcript id search
    transcript_id_regex = re.compile("transcript_id\s\"([^\";]+)")
    # transcript id search
    exon_regex = re.compile("exon_number\s\"([^\";]+)")
    # transcript id search
    gene_biotype_regex = re.compile("gene_biotype\s\"([^\";]+)")

    for i, entry in enumerate(entries):
        entry_info = entry[8]

        # check to see whether both gene id and transcript id exist
        try:
            gene_id = re.findall(gene_id_regex, entry_info)[0]
            transcript_id = re.findall(transcript_id_regex, entry_info)[0]
            gene_biotype = re.findall(gene_biotype_regex, entry_info)[0]
        except:
            transcript_id = None
            gene_id = None
            gene_biotype = None
            exon_number = None

        if transcript_id and gene_id and gene_biotype:
            try:
                exon_number = re.findall(exon_regex, entry_info)[0]
            except:
                exon_number = None
            # if given a list of transcript ids, check whether the entry is in those
            if transcript_ids and transcript_id not in transcript_ids:
                continue
            # if given a list of gene ids, check whether the entry is in those
            if gene_ids and gene_id not in gene_ids:
                continue
            # wanting a protein coding gene, check if entry matches
            if protein_coding and gene_biotype != "protein_coding":
                continue
            # if chromosomes to include, check if chromosome is in those
            if include_chrs and entry[0] not in include_chrs:
                continue
            # if chromosomes to exclude, check if chromosome is not in those
            if exclude_chrs and entry[0] not in exclude_chrs:
                continue
            # get the type of entry and check whether it exists in the features
            entry_type = entry[2]
            if entry_type not in features:
                continue
            # create the entry in bed format
            entry_id = "{0}.{1}".format(transcript_id, exon_number) if exon_number else transcript_id
            output = [entry[0], str(int(entry[3])-1), entry[4], entry_id, ".", entry[6], gene_id, entry_type]
            outputs.append(output)
    # if wanting to write to an output file, do so
    if output_file:
        with open(output_file, "w") as outfile:
            [outfile.write("{0}\n".format("\t".join(output))) for output in outputs]
    # return the entries
    return outputs
