"""Parse item."""


# --- import -------------------------------------------------------------------------------------


import ast
import numpy as np
import warnings


# --- functions -----------------------------------------------------------------------------------


def literal_eval(i):
    """Wrapper for ast.literal_eval which handles nan, inf, and -inf.
    """
    try:
        out = ast.literal_eval(i)
    except ValueError:
        if i == "nan":
            out = np.nan
        elif i == "inf":
            out = np.inf
        elif i == "-inf":
            out = -np.inf
        elif i[0:2] == "[[":  # case of multidimensional arrays
            warnings.warn(
                "Reading in multidimensional arrays with nan, inf, -inf is not a guaranteed behavior."
            )
            string = i
            replacements = [
                ("nan", 1e8, np.nan),
                ("inf", 1e9, np.inf),
                ("-inf", -1e9, -np.inf),
            ]  # not strictly safe
            for tup in replacements:
                string = string.replace(tup[0], str(tup[1]))
            out = ast.literal_eval(string)
            out = np.array(out)
            for tup in replacements:
                out[out == tup[1]] = tup[2]
        else:
            raise ValueError("could not parse the input {0}".format(i))
    return out
