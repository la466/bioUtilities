import numpy as np

def calc_pyrimidine(sequence):
    """
    Calculate the pyrimidine content of a sequence

    Parameters
    ---------
    sequence : str
        The sequence for calculating pyrimidine content

    Returns
    ---------
    pyrimidine_content : float
        Pyrimidine content of the sequence

    Examples
    ---------
    >>> from utilities.seq import calc_pyrimidine
    >>> calc_gc("ACATCGACTTGCTTA")
    0.6
    """

    pyrimidines = ["C", "T"]
    pyrimidine_content = np.divide(len([i for i in list(sequence) if i in pyrimidines]), len(sequence))
    return pyrimidine_content
