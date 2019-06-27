import numpy as np
import re

def motif_hit_positions(sequence, motifs, flatten = True):
    """
    Return the positions at which a motif in a set of motifs hits a sequence

    Parameters
    ---------
    sequence : str
        The sequence
    motifs : list
        The list of motifs to query for
    flatten : bool
        If set, flatten the hit list so its all hits. If false, this is the
        list of indices for each motif hit grouped by each hit

    Returns
    ---------
    motif_hits : list
        List of index positions where the motifs hit

    Examples
    ---------
    >>> from bioUtilities.seq import motif_hit_positions
    >>> calc_motif_density("ACATCGACTTGCTTA", ["CAT", "TTA"])
    [1, 2, 3, 12, 13, 14]
    """

    # create a regex containing all the motifs
    motif_search = re.compile("(?=({0}))".format("|".join(motifs)))
    # if the given item is a list of sequences, iterate through
    matches = re.finditer(motif_search, sequence)
    motif_hits = []
    # for each hit, add the indices for each position of the hit as a list to
    # the global list
    for hit in matches:
        motif_hits.append(list(range(hit.span()[0], hit.span()[0] + len(hit.group(1)))))
    # now flatten if we want just a list of all positions hit
    if flatten:
        temp_hits = []
        [temp_hits.extend(i) for i in motif_hits]
        motif_hits = temp_hits
        motif_hits = sorted(list(set(motif_hits)))

    return motif_hits
