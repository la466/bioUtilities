import numpy as np
import re

def calc_motif_density(sequences, motifs):
    """
    Calculate the density of a set of motifs in a sequence or list of sequences.
    Defined as the number of nucleotides hit by one of the motifs, divided by
    the total number of nucelotides

    Parameters
    ---------
    sequences : str, list
        The sequence or list of sequences for calculating motif density
    motifs : list
        The list of motifs to query for

    Returns
    ---------
    motif_density : float
        Motif density of the sequence or list of sequences

    Examples
    ---------
    >>> from bioUtilities.seq import calc_motif_density
    >>> calc_motif_density("ACATCGACTTGCTTA", ["TCG", "TTA"])
    0.4
    """

    seq_hits = 0
    seq_nts = 0
    # create a regex containing all the motifs
    motif_search = re.compile("(?=({0}))".format("|".join(motifs)))
    # if the given item is a list of sequences, iterate through
    if isinstance(sequences, list):
        for i, seq in enumerate(sequences):
            hits = []
            matches = re.finditer(motif_search, seq)
            [hits.extend(list(range(hit.span()[0], hit.span()[0] + len(hit.group(1))))) for hit in matches]
            hits = sorted(list(set(hits)))
            seq_nts += len(seq)
            seq_hits += len(hits)
    # otherwise, just calculate the density
    else:
        matches = re.finditer(motif_search, sequences)
        hits = []
        [hits.extend(list(range(hit.span()[0], hit.span()[0] + len(hit.group(1))))) for hit in matches]
        hits = sorted(list(set(hits)))
        seq_nts += len(sequences)
        seq_hits += len(hits)
    motif_density = np.divide(seq_hits, seq_nts)
    return motif_density
