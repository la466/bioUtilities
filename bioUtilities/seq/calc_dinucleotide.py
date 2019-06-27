import numpy as np
import collections
import re

def calc_dinucleotide(sequences):
    """
    Calculate the dinucleotide content of a sequence or a list of sequences

    Parameters
    ---------
    sequences : str, list
        The sequence or list of sequences to calculate

    Returns
    ---------
    dinucleotide_content : dict
        Dinucleotide content of the sequence or sequences

    Examples
    ---------
    >>> from bioUtilities.seq import calc_dinucleotide
    >>> calc_dinucleotide("ACGAC")
    {"AC": 0.5, "CG": 0.25, "GA": 0.25}
    >>> calc_dinucleotide(["ACGAT", "ACTAG"])
    {"AC": 0.25, "AG": 0.125, "AT": 0.125, "CG": 0.125, "CT": 0.125, "GA": 0.125, "TA": 0.125}
    """

    dinucleotide_search = re.compile(".{2}")
    dinucleotide_counts = collections.Counter()
    # if a list of sequences, do the combined
    if isinstance(sequences, list):
        for i, seq in enumerate(sequences):
            for frame in [0, 1]:
                matches = re.findall(dinucleotide_search, seq[frame:])
                for match in matches:
                    dinucleotide_counts[match] += 1
    # otherwise, just calculate for the single sequence
    else:
        for frame in [0, 1]:
            matches = re.findall(dinucleotide_search, sequences[frame:])
            for match in matches:
                dinucleotide_counts[match] += 1

    total = sum(dinucleotide_counts.values())
    dicnucleotide_content = {i: np.divide(dinucleotide_counts[i], total) for i in sorted(dinucleotide_counts)}
    return dicnucleotide_content
