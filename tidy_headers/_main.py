"""Main."""


# --- import -------------------------------------------------------------------------------------


import re
import collections

from ._parse_item import item2string, string2item


# --- define -------------------------------------------------------------------------------------


__all__ = ['read', 'write']


# --- helpers ------------------------------------------------------------------------------------


def read(filepath):
    """Read 'WrightTools formatted' headers from given path.
    Parameters
    ----------
    filepath : str
        Path of file.
    Returns
    -------
    OrderedDict
        Dictionary containing header information.
    See Also
    --------
    kit.write_headers
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
    """Write 'WrightTooTools formatted' headers to given file.
    Headers written can be read again using read_headers.
    Parameters
    ----------
    filepath : str
        Path of file. File must not exist.
    dictionary : dict or OrderedDict
        Dictionary of header items.
    Returns
    -------
    str
        Filepath of file.
    See Also
    --------
    kit.read_headers
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
    # return
    return filepath
