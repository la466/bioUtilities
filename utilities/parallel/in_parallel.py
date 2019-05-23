from utilities.parallel import multiprocess
import os
import multiprocessing
import collections

def in_parallel(iteration_list, arguments, function_to_run, kwargs_dict = None, parallel = True, workers = None):
    """
    A wrapper to run a function in parallel. Tries to give the same output as if
    the function was being run linearly.

    Parameters
    ---------
        iteration_list : list
            The list of items to iterate over
        arguments : list
            A list of arguments to pass to the function
        function_to_run : func
            The function to run in parallel
        kawrgs_dict : dict
            A dictionary of keyword argument to pass to the function
        parallel: bool
            If true, run in parallel, else run linearly
        workers : int
            If set, use user defined number of processes


    Returns
    ---------
        outputs : variable
            The output of the function_to_run

    Examples
    ---------
    >>> from utilities.parallel import in_parallel
    >>> in_parallel(["gene1", "gene2", "gene3"], [{"gene1": "ATGACTAG", "gene2": "ATGCGCAATAG", "gene3": "ATGCCCTAA"}], calculate_gc_content)
    """

    print(multiprocess)

    # run the simulations
    if parallel:
        # add foo to argument list for parallelisation
        arguments.insert(0, "foo")
        # get the number of workers to use
        if not workers:
            # minus 2 to allow some spare cpus
            workers = os.cpu_count() - 2
        # run the function
        if parallel:
            one_by_one = None
        else:
            one_by_one = True
        # run process
        processes = multiprocess(iteration_list, arguments, function_to_run, kwargs_dict = kwargs_dict, workers = workers, one_by_one = one_by_one)
        # now process the results
        # first get the results
        results = []
        for process in processes:
            results.append(process.get())
        # now merge into one
        # if you return a list from the function, combine the lists
        if isinstance(results[0], list):
            flattened_outputs = []
            [flattened_outputs.extend(i) for i in results]
            outputs = flattened_outputs
        # if you return a dictionary
        elif isinstance(results[0], dict):
            # get the keys
            keys = list(results[0].keys())
            # if keys exist
            if len(keys):
                # if the results have repeated keys, append each keys result to a list to merge all results
                # for one key to the same list
                if isinstance(results[0][keys[0]], list):
                    flattened_outputs = collections.defaultdict(lambda: [])
                    for result in results:
                        for key in result:
                            flattened_outputs[key].extend(result[key])
                    #unpickle
                    outputs = {i: flattened_outputs[i] for i in flattened_outputs}
                # otherwise, just add to one dictionary
                else:
                    flattened_outputs = {}
                    [flattened_outputs.update(i) for i in results]
                    outputs = flattened_outputs
            else:
                outputs = None
        else:
            outputs = None
    else:
        if kwargs_dict:
            # use keyword args
            outputs = function_to_run(simulations, *arguments, **kwargs_dict)
        else:
            # no keyword args
            outputs = function_to_run(simulations, *arguments)
    # return the outputs
    return outputs
