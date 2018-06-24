"""Parse array."""


# --- import -------------------------------------------------------------------------------------


import ast
import re

import numpy as np


# --- parse --------------------------------------------------------------------------------------


def array2string(array, sep="\t"):
    """Generate a string from an array with useful formatting.

    Great for writing arrays into single lines in files.

    See Also
    --------
    string2array
    """
    np.set_printoptions(threshold=array.size)
    string = np.array2string(array, separator=sep)
    string = string.replace(sep.strip() + "\n", sep)
    string = re.sub(r"({})(?=\1)".format(sep), "", string)
    return string


def string2array(string, sep="\t"):
    """Generate an array from a string created using array2string.

    See Also
    --------
    array2string
    """
    string = string.replace(sep, ",")
    string = re.sub(",,+", ",", string)
    return np.array(ast.literal_eval(string))
