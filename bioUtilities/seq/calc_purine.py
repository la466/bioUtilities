import numpy as np

def calc_purine(sequence):
    """
    Calculate the purine content of a sequence

    Parameters
    ---------
    sequence : str
        The sequence for calculating purine content

    Returns
    ---------
    purine_content : float
        Purine content of the sequence

    Examples
    ---------
    >>> from bioUtilities.seq import calc_purine
    >>> calc_gc("ACATCGACTTGCTTA")
    0.4
    """

    purines = ["A", "G"]
    purine_content = np.divide(len([i for i in list(sequence) if i in purines]), len(sequence))
    return purine_content
