import numpy as np
import collections
import re

def calc_nucleotide(sequences):
    """
    Calculate the nucleotide content of a sequence or a list of sequences

    Parameters
    ---------
    sequences : str, list
        The sequence or list of sequences to calculate

    Returns
    ---------
    nucleotide_content : dict
        Nucleotide content of the sequence or sequences

    Examples
    ---------
    >>> from bioUtilities.seq import calc_nucleotide
    >>> calc_nucleotide("ACGAC")
    {"A": 0.4, "C": 0.4, "G": 0.2}
    >>> calc_nucleotide(["ACGAT", "ACTAG"])
    {"A": 0.4, "C": 0.2, "G": 0.2, "T": 0.2}
    """

    # if a list of sequences, concatenate
    if isinstance(sequences, list):
        sequences = "".join(sequences)
    nucleotides = list(sequences)
    nucleotide_count = collections.Counter()
    for nt in ["A", "C", "G", "T"]:
        nucleotide_count[nt] += nucleotides.count(nt)
    total = sum(nucleotide_count.values())
    nucleotide_content = {i: np.divide(nucleotide_count[i], total) for i in sorted(nucleotide_count)}
    return nucleotide_content
