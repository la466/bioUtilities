import os
import multiprocessing

def multiprocess(input_list, arguments, function_to_run, kwargs_dict = None, workers = None, onebyone = False, main_function = None):
    """
    Take an input list, chunk up the list and then apply a function_to_runtion to each
    of the chunk in parallel.

    Parameters
    ---------
    input_list : list
        A list of the things you want to iterate over in parallel (for
        example, a list of gene names)
    arguments : list
        A list of arguments supplied to function_to_runtion. Put in "foo" in
        place of the argument you are parallelizing over.
    function_to_run : func
        The function you want to parallellise
    kwargs_dict : dict
        A dictionary of any keyword arguments the function_to_runtion might take
    workers : int
        A user defined number of parallel processes to launch
    onebyone : bool
        If True, allocate one element from input_list to each process


    Returns
    ---------
    results : variable
        The results of the funcion to run

    Examples
    ---------
    >>> from utilities.parallel import multiprocess
    >>> multiprocess(["gene1", "gene2", "gene3"], [{"gene1": "ATGACTAG", "gene2": "ATGCGCAATAG", "gene3": "ATGCCCTAA"}], calculate_gc_content)

    Credits
    ---------
    Rosina Savisaar
    """

    if not workers:
        # subtract one to leave one worker free
        workers = int(os.cpu_count() - 1)
    elif workers == "all":
        workers = os.cpu_count()
    #in the list of arguments, I put in "foo" for the argument that corresponds to whatever is in the input_list because I couldn't be bothered to do something less stupid
    arg_to_parallelize = arguments.index("foo")
    if not onebyone:
        #divide input_list into as many chunks as you're going to have processes
        chunk_list = [input_list[i::workers] for i in range(workers)]
    else:
        #each element in the input list will constitute a chunk of its own.
        chunk_list = input_list

    kwargs_dict = {}
    kwargs_dict["main_function"] = function_to_run

    pool = multiprocessing.Pool(workers)
    results = []
    #go over the chunks you made and laucnh a process for each
    for elem in chunk_list:
        current_arguments = arguments.copy()
        current_arguments[arg_to_parallelize] = elem

        if kwargs_dict:
            process = pool.apply_async(function_to_run, tuple(current_arguments), kwargs_dict)
        else:
            process = pool.apply_async(function_to_run, tuple(current_arguments))
        results.append(process)
    pool.close()
    pool.join()
    return results
