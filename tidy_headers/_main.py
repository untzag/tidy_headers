"""Main."""


# --- import -------------------------------------------------------------------------------------


import re
import copy
import collections

import numpy as np

from ._parse_item import item2string, string2item


# --- define -------------------------------------------------------------------------------------


__all__ = ['read', 'write']


# --- helpers ------------------------------------------------------------------------------------


def read(filepath):
    """Read headers from given filepath.

    Parameters
    ----------
    filepath : str
        Path of file.

    Returns
    -------
    collections.OrderedDict
        Dictionary containing header information.
    """
    headers = collections.OrderedDict()
    for line in open(filepath):
        if line[0] == '#':
            split = re.split('\: |\:\t', line)
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
        if '\t' in value:
            joiner = ''
        else:
            joiner = '\t'
        lines.append(joiner.join([key + ':', value]))
    header_str = '\n'.join(lines)
    np.savetxt(filepath, [], header=header_str)
