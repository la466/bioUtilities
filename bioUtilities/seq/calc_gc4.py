from utilities.seq import calc_gc3
from utilities.useful_sets import fourfolds
import numpy as np
import re

def calc_gc4(sequence):
    """
    Calculate the GC4 content of a sequence

    Parameters
    ---------
    sequence : str
        The sequence for calculating GC content

    Returns
    ---------
    gc4 : float
        GC4 content of the sequence

    Examples
    ---------
    >>> from utilities.seq import calc_gc4
    >>> calc_gc4("ACATCGACTTGC")
    0.5
    """

    # first get fourfold degenerate codons
    sequence_fourfold_codons = [i for i in re.findall(".{3}", sequence) if i in fourfolds]
    # now calculate gc3 of those codons
    gc4 = calc_gc3("".join(sequence_fourfold_codons))
    return gc4
