import re
import collections
import numpy as np
import itertools as it


def get_dinucleotide_content(sequence):
    """
    Calculate the dinucleotide content of a sequence

    Parameters
    ---------
    sequence : str
        The sequence for calculating dinucleotide content

    Returns
    ---------
    dinucleotide_content : dict
        Dinucleotide content of a the sequence

    Examples
    ---------
    >>> from bioUtilities.seq import get_dinucleotide_content
    >>> get_dinucleotide_content("GACTGA")
    {'AC': 0.2, 'CT': 0.2, 'GA': 0.4, 'TG': 0.2}
    """

    # set up the regex and counts
    dinucleotide_regex = re.compile('.{2}')
    dinucleotide_list = ["".join(i) for i in it.product("ACGT", repeat=2)]
    dinucleotide_count = collections.defaultdict(lambda: 0)
    # get the dinucleotides
    dinucleotides1 = re.findall(dinucleotide_regex, sequence)
    dinucleotides2 = re.findall(dinucleotide_regex, sequence[1:])
    # get the total dinucleotides
    total_dinucleotides =  len(dinucleotides1) + len(dinucleotides2)
    # get the counts
    for dint in dinucleotide_list:
        dinucleotide_count[dint] += dinucleotides1.count(dint)
        dinucleotide_count[dint] += dinucleotides2.count(dint)
    # now get the dinucleotide use as a proportion
    dinucleotide_content = {}
    for i, count in sorted(dinucleotide_count.items()):
        if count != 0:
            dinucleotide_content[i] = np.divide(count, total_dinucleotides)

    return dinucleotide_content
