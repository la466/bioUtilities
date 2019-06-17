import numpy as np

def calc_gc(sequence):
    """
    Calculate the GC content of a sequence

    Parameters
    ---------
    sequence : str
        The sequence for calculating GC content

    Returns
    ---------
    gc : float
        GC content of the sequence

    Examples
    ---------
    >>> from utilities.seq import calc_gc
    >>> calc_gc("ACATCGACTTGC")
    0.5
    """

    gc = np.divide(sum([1 for i in list(sequence) if i in ["G", "C"]]), len(sequence))
    return gc
