import os

def create_directory(path):
    """
    Create a diretory given a path. Iterate through all parent directories to
    create those too if they do not already exist.

    Parameters
    ---------
    path : str
        Path of the directory to create

    Examples
    ---------
    >>> from bioUtilities.dir import create_directory
    >>> create_directory("test_directory/another_directory")
    """

    path_splits = path.split('/')
    new_path = []
    for i, split in enumerate(path_splits):
        if len(split) > 0:
            new_path.append(split)
            current_path = "/".join(new_path)
            if not os.path.exists(current_path):
                os.makedirs(current_path, exist_ok=True)
