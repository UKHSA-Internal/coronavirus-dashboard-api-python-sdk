#!/usr/bin python3

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
from typing import NoReturn

# 3rd party:

# Internal: 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'save_data'
]


def save_data(data: str, path: str, ext: str) -> NoReturn:
    """
    Saves the data in a file.

    Parameters
    ----------
    data: str
        Data to be saved.

    path: str
        Path (relative or absolute) to the file in which
        the data is to be saved. The path must end with
        the value defined for the ``ext`` argument.

    ext: str
        Extension (type) of the file --- e.g. ``json``.

    Returns
    -------
    NoReturn
    """
    from os import access, W_OK, path as os_path

    if os_path.isdir(path):
        raise IsADirectoryError(
            'No file name: The log file path must define an '
            'absolute path and a filename. Currently: <{filepath}>.'
        )
    elif not path.lower().endswith(ext.lower()):
        _, current_ext = os_path.splitext(path)
        raise ValueError(
            "The path does not end with the correct extension "
            f"for this format. Expected a file ending with '.{ext}', "
            f"got '{current_ext}' instead."
        )

    abs_path = os_path.abspath(path)
    file_dir = os_path.dirname(abs_path)

    if not os_path.isdir(file_dir):
        raise NotADirectoryError(
            f"The parent directory for the file '{path}' must "
            f"already exist."
        )

    if not access(file_dir, W_OK):
        from getpass import getuser

        raise PermissionError(
            f"Current user ({getuser()}) does not have 'write' "
            f"permission for <{file_dir}>."
        )

    with open(abs_path, "w") as pointer:
        print(data, file=pointer)
