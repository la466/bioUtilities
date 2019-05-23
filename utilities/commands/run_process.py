import subprocess

def run_process(arguments, return_string = True, input_to_pipe = None, return_error = False, file_for_input = None, file_for_output = None, universal_newlines = True, shell = False):
    """
    Run a command on the command line. Supply command as a list of strings.

    Parameters
    ---------
        arguments : list
            Arguments that you want to run
        return_string : bool
            Return the process output as a string
        input_to_pipe : variable
            If set, will use the output of another process as input to function
        return_error : bool
            If true, return the error
        file_for_input : str
            If set, the path to a file used for input
        file_for_output : str
            If set, the file used for output
        universal_newlines : bool
            If set, think of as text
        shell : bool
            If set, the command will be run through the shell


    Returns
    ---------
        stderr : variable
            The error message
        stdout : variable
            The output

    Examples
    ---------
    >>> from utilities.commands import run_process
    >>> run_process(["touch", "test_file.txt"])

    Credits
    ---------
    Rosina Savisaar
    """

    if file_for_input:
        input_file = open(file_for_input)
        stdin_src = input_file
    else:
        stdin_src = subprocess.PIPE
    if file_for_output:
        output_file = open(file_for_output, "w")
        stdout_dest = output_file
    else:
        stdout_dest = subprocess.PIPE
    arguments = [str(i) for i in arguments]
    if shell:
        arguments = " ".join(arguments)
    process = subprocess.Popen(arguments, shell = shell, stdout = stdout_dest, stderr = subprocess.PIPE,
                               stdin = stdin_src, universal_newlines = universal_newlines)
    if input_to_pipe:
        stdout, stderr = process.communicate(input_to_pipe)
    else:
        stdout, stderr = process.communicate()
    if file_for_input:
        input_file.close()
    if file_for_output:
        output_file.close()
    return_code = process.poll()
    if return_code != 0:
        print("Process failed!")
        print(" ".join(arguments))
        print(stderr)
        return("error")
    #if the process returns bytes but you want to get a string back.
    if return_string and type(stdout) == bytes:
        stdout = stdout.decode("utf-8")
    if return_error:
        return(stderr)
    else:
        return(stdout)
