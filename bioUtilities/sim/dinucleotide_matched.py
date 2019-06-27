from bioUtilities.seq import calc_dinucleotide, calc_nucleotide
import numpy as np

def dinucleotide_matched(sequences, set_seed = True, seed = None):
    """
    Generate dinucleotide matched sequences given sequences

    Parameters
    ---------
    sequences : str, list
        The sequence/sequences for generating matched sequences
    set_seed : bool
        Determine whether to set the seed in the function. Useful to set as
        false if doing in parallel
    seed : int
        If set, the randomisation seed

    Returns
    ---------
    dinucleotide_matched : str, list
        Dinucleotide matched random sequence

    Examples
    ---------
    >>> from bioUtilities.seq import dinucleotide_matched
    >>> dinucleotide_matched("CATGA")
    TGATC
    >>> dinucleotide_matched(["CATGA", "ACTAG"])
    ["TGATC", "GACAT"]
    """

    # set the randomisation seed
    if set_seed:
        np.random.seed(seed)

    # if just one sequence, put in list for later
    if isinstance(sequences, str):
        sequences = [sequences]

    dinucleotide_content = calc_dinucleotide(sequences)
    dinucleotide_probs = [dinucleotide_content[i] for i in sorted(dinucleotide_content)]
    nucleotide_content = calc_nucleotide(sequences)
    nucleotide_probs = [nucleotide_content[i] for i in sorted(nucleotide_content)]

    dinucleotide_matched = []

    for sequence in sequences:
        required_dinucleotides = int(len(sequence) / 2)
        required_nucleotides = len(sequence) % 2
        new_seq = list(np.random.choice(list(sorted(dinucleotide_content)), size = required_dinucleotides, p = dinucleotide_probs))
        if required_nucleotides > 0:
            new_seq.extend(np.random.choice(list(sorted(nucleotide_content)), size = required_nucleotides, p = nucleotide_probs))
        dinucleotide_matched.append("".join(new_seq))

    if len(sequences) == 1:
        dinucleotide_matched = dinucleotide_matched[0]
    return dinucleotide_matched
