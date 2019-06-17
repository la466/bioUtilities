import numpy as np

def calc_gc3(sequence):
    """
    Calculate the GC3 content of a sequence

    Parameters
    ---------
    sequence : str
        The sequence for calculating GC content

    Returns
    ---------
    gc3 : float
        GC3 content of the sequence

    Examples
    ---------
    >>> from utilities.seq import calc_gc3
    >>> calc_gc3("ACATCGACTTGC")
    0.5
    """

    third_sites = [sequence[j] for j in [i+2 for i in list(range(0, len(sequence), 3))]]
    gc3 = np.divide(sum([1 for i in third_sites if i in ["G", "C"]]), len(third_sites))
    return gc3
