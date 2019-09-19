"""Main."""


# --- import -------------------------------------------------------------------------------------


import re
import os
import copy
import collections

import numpy as np

from ._parse_item import item2string, string2item


# --- define -------------------------------------------------------------------------------------


__all__ = ["read", "write"]


# --- helpers ------------------------------------------------------------------------------------


def read(filepath, *, encoding="utf-8"):
    """Read headers from given filepath.

    Parameters
    ----------
    filepath : path-like or iterable of strings
        Path to file or iterable of stings
    encoding : str
        Encoding to use when opening the file.
        No effect if iterable of strings given.

    Returns
    -------
    collections.OrderedDict
        Dictionary containing header information.
    """
    headers = collections.OrderedDict()
    ds = np.DataSource(None)
    # The following code is adapted from np.genfromtxt source
    try:
        if isinstance(filepath, os.PathLike):
            filepath = os.fspath(filepath)
        if isinstance(filepath, str):
            fhd = iter(ds.open(filepath, 'rt', encoding=encoding))
        else:
            fhd = iter(filepath)
    except TypeError:
        raise TypeError(
            "filepath must be a path-like, list of strings, "
"or generator. Got %s instead." % type(filepath))
    for line in fhd:
        if line[0] == "#":
            split = re.split(": |:\t", line, maxsplit=1)
            key = split[0][2:]
            headers[key] = string2item(split[1])
        else:
            break  # all header lines are at the beginning
    return headers


def write(filepath, dictionary):
    """Write headers to given filepath.

    Parameters
    ----------
    filepath : str
        Path of file. File must not yet exist.
    dictionary : dict or OrderedDict
        Dictionary of header items.
    """
    dictionary = copy.deepcopy(dictionary)
    # write header
    for key, value in dictionary.items():
        dictionary[key] = item2string(value)
    lines = []
    for key, value in dictionary.items():
        if "\t" in value:
            joiner = ""
        else:
            joiner = "\t"
        lines.append(joiner.join([key + ":", value]))
    header_str = "\n".join(lines)
    np.savetxt(filepath, [], header=header_str)
