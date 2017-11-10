"""Parse array."""


# --- import -------------------------------------------------------------------------------------


import re

import numpy as np

from ._utilities import flatten_list


# --- parse --------------------------------------------------------------------------------------


def array2string(array, sep='\t'):
    """Generate a string from an array with useful formatting.

    Great for writing arrays into single lines in files.

    See Also
    --------
    string2array
    """
    np.set_printoptions(threshold=array.size)
    string = np.array2string(array, separator=sep)
    string = string.replace('\n', sep)
    string = re.sub(r'({})(?=\1)'.format(sep), '', string)
    return string


def string2array(string, sep='\t'):
    """Generate an array from a string created using array2string.

    See Also
    --------
    array2string
    """
    # discover size
    size = string.count('\t') + 1
    # discover dimensionality
    dimensionality = 0
    while string[dimensionality] == '[':
        dimensionality += 1
    # discover shape
    shape = []
    for i in range(1, dimensionality + 1)[::-1]:
        to_match = '[' * (i - 1)
        count_positive = string.count(to_match + ' ')
        count_negative = string.count(to_match + '-')
        shape.append(count_positive + count_negative)
    shape[-1] = size / shape[-2]
    for i in range(1, dimensionality - 1)[::-1]:
        shape[i] = shape[i] / shape[i - 1]
    shape = tuple([int(s) for s in shape])
    # import list of floats
    lis = string.split(' ')
    # annoyingly series of negative values get past previous filters
    lis = flatten_list([i.split('-') for i in lis])
    for i, item in enumerate(lis):
        bad_chars = ['[', ']', '\t', '\n']
        for bad_char in bad_chars:
            item = item.replace(bad_char, '')
        lis[i] = item
    for i in range(len(lis))[::-1]:
        try:
            lis[i] = float(lis[i])
        except ValueError:
            lis.pop(i)
    # create and reshape array
    arr = np.array(lis)
    arr.shape = shape
    # finish
    return arr
