import argparse

def parse_arguments(arguments, description = None, floats = [], ints = [], flags = [], opt_flags = []):
    """
    Parse a set of arguments from the command line.

    Parameters
    ---------
    arguments : list
        List of arguments that you want to run
    description: str
        If set, a description of the aguments you want to run
    floats : list
        List of indices that correspond to the arguments that are floats
    ints : list
        List of indices that correspond to the arguments that are integers
    flags : list
        List of indices that correspond to the arguments that are flags
    opt_flags : list
        List of indices that correspond to the arguments that are optional flags
        that also take a user defined value

    Returns
    ---------
    args : list
        List of processed arguments

    Examples
    ---------
    >>> from bioUtilities.commands import parse_arguments
    >>> args = parse_arguments(["arg1", "arg2", 1], ints = [2])

    Credits
    ---------
    Rosina Savisaar
    """

    parser = argparse.ArgumentParser(description = description)
    for pos, argument in enumerate(arguments):
        if pos in flags:
            parser.add_argument("--{0}".format(argument), action = "store_true", help = argument)
        elif pos in opt_flags:
            parser.add_argument("-{0}".format(argument), action = "store", dest = "{0}".format(argument))
        else:
            if pos in floats:
                curr_type = float
            elif pos in ints:
                curr_type = int
            else:
                curr_type = str
            parser.add_argument(argument, type = curr_type, help = argument)
    args = parser.parse_args()
    return args
