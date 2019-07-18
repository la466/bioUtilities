from __future__ import print_function
import bioUtilities.parallel
import os
import multiprocessing
import collections
import numpy as np
import time
import random
from concurrent.futures import ProcessPoolExecutor, as_completed


def run_parallelisation(*args, **kwargs):
    function_to_run = kwargs["function_to_run"]
    del kwargs["function_to_run"]
    chunk = kwargs["chunk"]
    del kwargs["chunk"]
    randomisation = kwargs["randomisation"]
    del kwargs["randomisation"]
    pass_iteration = kwargs["pass_iteration"]
    del kwargs["pass_iteration"]

    outputs = []
    if len(chunk) != 0:
        if randomisation:
            np.random.seed()
        for i, item in enumerate(chunk):
            kwargs_local = kwargs.copy()
            # if we want to pass the id of the iteration into the function
            if pass_iteration:
                # kwargs_local["iteration"] = item
                output = function_to_run(item, *args, **kwargs_local)
            else:
                output = function_to_run(*args, **kwargs_local)
            outputs.append(output)
    return outputs



def in_parallel(function_to_run, iteration_list, args = [], randomisation = None, pass_iteration = True, kwargs = None, parallel = True, workers = None):
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
    >>> from bioUtilities.parallel import in_parallel
    >>> in_parallel(["gene1", "gene2", "gene3"], [{"gene1": "ATGACTAG", "gene2": "ATGCGCAATAG", "gene3": "ATGCCCTAA"}], calculate_gc_content)
    """

    if not function_to_run or not iteration_list:
        raise Exception("\n\nERROR: Both the function to run and the list to iterate over are required.\n")


    # run the simulations
    if parallel:
        # add foo to argument list for parallelisation
        # arguments.insert(0, "foo")
        # get the number of workers to use
        if not workers:
            # minus 2 to allow some spare cpus
            workers = os.cpu_count() - 2
            # workers = 2
        # run the function
        one_by_one = False

        pool = multiprocessing.Pool(workers)
        # because this a randomisation, we only want to call the random seed
        # once rather than each time we run the function
        # so first chunk the iteration list between the workers
        chunk_list = [iteration_list[i::workers] for i in range(workers)]
        outputs = []
        # now for each chunk, copy the kwargs_dict and add the function to
        # run and chunk to the arguments
        # the run through the randomisastion parallel function and get the
        # outputs

        print("Multiprocessing: {0} workers available, {1} workers inititated".format(os.cpu_count(), len([i for i in chunk_list if len(i) > 0])))

        for chunk in chunk_list:
            if kwargs:
                kwargs_local = kwargs.copy()
                kwargs_local["function_to_run"] = function_to_run
                kwargs_local["chunk"] = chunk
                kwargs_local["pass_iteration"] = chunk
                kwargs_local["randomisation"] = randomisation

            else:
                kwargs_local = {"function_to_run" : function_to_run, "chunk": chunk, "pass_iteration" : pass_iteration, "randomisation" : randomisation}
            process = pool.apply_async(run_parallelisation, args = tuple(args.copy()), kwds = kwargs_local)
            outputs.append(process)

        # now get each of the results
        results = []
        for output in outputs:
            results.extend(output.get())

        return results

        pool.close()
        pool.join()
