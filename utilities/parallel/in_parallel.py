from __future__ import print_function
import utilities.parallel
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
            # print("{0}: {1}/{2}",format(i, len(chunk)))
            kwargs_local = kwargs.copy()
            # if we want to pass the id of the iteration into the function
            if pass_iteration:
                kwargs_local["iteration"] = item
            output = function_to_run(*args, **kwargs_local)
            outputs.append(output)
    return outputs



def in_parallel(function_to_run = None, args = None, iteration_list = None, randomisation = None, pass_iteration = None, kwargs = None, parallel = True, workers = None):
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
        if parallel:
            one_by_one = None
        else:
            one_by_one = True

        pool = multiprocessing.Pool(workers)
        print("{0} workers initiated.".format(workers))
        # because this a randomisation, we only want to call the random seed
        # once rather than each time we run the function
        # so first chunk the iteration list between the workers
        chunk_list = [iteration_list[i::workers] for i in range(workers)]
        outputs = []
        # now for each chunk, copy the kwargs_dict and add the function to
        # run and chunk to the arguments
        # the run through the randomisastion parallel function and get the
        # outputs
        for chunk in chunk_list:
            if kwargs:
                kwargs_local = kwargs.copy()
                kwargs_local["function_to_run"] = function_to_run
                kwargs_local["chunk"] = chunk
                kwargs_local["pass_iteration"] = chunk
                kwargs_local["randomisastion"] = randomisation

            else:
                kwargs_local = {"function_to_run" : function_to_run, "chunk": chunk, "pass_iteration" : pass_iteration, "randomisation" : randomisation}
            process = pool.apply_async(run_parallelisation, args = tuple(args.copy()), kwds = kwargs_local)
            outputs.append(process)

        # now get each of the results
        results = []
        for output in outputs:
            results.extend(output.get())

        print(results)

        pool.close()
        pool.join()
        # pool.clear()

        # results = results.get()
        # print(results)
        # results = [pool.apply_async(calculate, t) for t in TASKS]
        # imap_it = pool.imap(calculatestar, TASKS)
        # imap_unordered_it = pool.imap_unordered(calculatestar, TASKS)

        # print 'Ordered results using pool.apply_async():'

        # results_list = []
        # for r in results:
        #     if r.get():
        #         results_list.append(r.get())
        #
        # if isinstance(results_list[0], dict):
        #     flattened_outputs = {}
        #     [flattened_outputs.update(i) for i in results_list]
        #     outputs = flattened_outputs
        # print(outputs)



        # processes = utilities.parallel.multiprocess(iteration_list, arguments, local_in_parallel, main_function = function_to_run, kwargs_dict = kwargs_dict, workers = workers, onebyone = one_by_one)

    #     for process in processes:
    #         print(process)
    #
    #     # now process the results
    #     # first get the results
    #     results = []
    #     for process in processes:
    #         results.append(process.get())
    #     # now merge into one
    #     # if you return a list from the function, combine the lists
    #     if isinstance(results[0], list):
    #         flattened_outputs = []
    #         [flattened_outputs.extend(i) for i in results]
    #         outputs = flattened_outputs
    #     # if you return a dictionary
    #     elif isinstance(results[0], dict):
    #         # get the keys
    #         keys = list(results[0].keys())
    #         # if keys exist
    #         if len(keys):
    #             # if the results have repeated keys, append each keys result to a list to merge all results
    #             # for one key to the same list
    #             if isinstance(results[0][keys[0]], list):
    #                 flattened_outputs = collections.defaultdict(lambda: [])
    #                 for result in results:
    #                     for key in result:
    #                         flattened_outputs[key].extend(result[key])
    #                 #unpickle
    #                 outputs = {i: flattened_outputs[i] for i in flattened_outputs}
    #             # otherwise, just add to one dictionary
    #             else:
    #                 flattened_outputs = {}
    #                 [flattened_outputs.update(i) for i in results]
    #                 outputs = flattened_outputs
    #         else:
    #             outputs = None
    #     else:
    #         outputs = None
    # else:
    #     if kwargs_dict:
    #         # use keyword args
    #         outputs = function_to_run(simulations, *arguments, **kwargs_dict)
    #     else:
    #         # no keyword args
    #         outputs = function_to_run(simulations, *arguments)
    # # return the outputs
    # return outputs


def local_in_parallel(iteration_list, *args, main_function = None, random_seed = None):
    output = []
    if len(iteration_list):
        np.random.seed()

        for i, iteration in enumerate(iteration_list):
            main_function(args)

    return output
    # print(kawrgs_dict)
    # print(main_function)
    #
    # for i, iteration in enumerate(iteration_list):
    #     local_output = main_function(args)
    #     local_output = kwargs_dict["function_to_run"](args)
    #     print(iteration_list)
    #     print(args)
    #     print(kwargs_dict)
    # print(function_to_run)
