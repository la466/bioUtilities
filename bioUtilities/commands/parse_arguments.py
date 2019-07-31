import argparse

def parse_arguments(arguments, description = None, listed_args = None):
    """
    Parse a set of arguments from the command line.

    Parameters
    ---------
    arguments : list
        List of arguments that you want to run
    description: str
        If set, a description of the aguments you want to run
    listed_args : list, opt
        If set, a list of arguments given to preserve argument order

    Returns
    ---------
    args : list
        List of processed arguments

    Examples
    ---------
    >>> from bioUtilities.commands import parse_arguments
    >>> arguments = arguments = {"arg1": str, "arg2": float, "arg3": int, "arg4": "flag", "arg5": "opt"}
    >>> args = parse_arguments(arguments)
    """

    if not listed_args:
        listed_args = list(arguments)

    parser = argparse.ArgumentParser(description = description)
    for argument in listed_args:
        if arguments[argument] == "flag":
            parser.add_argument("--{0}".format(argument), action = "store_true", help = argument)
        elif arguments[argument] == "opt":
            parser.add_argument("-{0}".format(argument), action = "store", dest = "{0}".format(argument))
        elif arguments[argument] == float:
            parser.add_argument(argument, type = float, help = argument)
        elif arguments[argument] == int:
            parser.add_argument(argument, type = int, help = argument)
        else:
            parser.add_argument(argument, type = str, help = argument)
    args = parser.parse_args()
    return args
