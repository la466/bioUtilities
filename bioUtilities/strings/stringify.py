def stringify(input):
    """
    Turn the input into strings

    Parameters
    ---------
    input : str, list
        The input to be converted to string

    Returns
    ---------
    output : str, list
        Converted input

    Examples
    ---------
    >>> from bioUtilities.strings import stringify
    >>> stringify(1)
    "1"
    """

    # if a list of items, do it for each
    if isinstance(input, list):
        output = [str(i) for i in input]
    # otherwise, just do it for single item
    else:
        output = str(input)

    return output
