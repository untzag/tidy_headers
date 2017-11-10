"""Parse item."""


# --- import -------------------------------------------------------------------------------------


import ast

from ._parse_array import array2string, string2array


# --- functions ----------------------------------------------------------------------------------


def item2string(item, sep='\t'):
    r"""Generate string from item.
    Parameters
    ----------
    item : object
        Item.
    sep : string (optional)
        Separator. Default is '\t'.
    Returns
    -------
    string
    See Also
    --------
    string2item
    """
    out = ''
    if isinstance(item, string_type):
        out += '\'' + item + '\''
    elif isinstance(item, list):
        for i in range(len(item)):
            if isinstance(item[i], string_type):
                item[i] = '\'' + item[i] + '\''
            else:
                item[i] = str(item[i])
        out += ' [' + sep.join(item) + ']'
    elif type(item).__module__ == np.__name__:  # anything from numpy
        if hasattr(item, 'shape'):
            out = ' ' + array2string(item, sep=sep)
        else:
            out += ' [' + sep.join([str(i) for i in item]) + ']'
    else:
        out = str(item)
    return out


def string2item(string, sep='\t'):
    r"""Turn a string into a python object.
    Parameters
    ----------
    string : string
        String.
    sep : string (optional)
        Seperator. Default is '\t'.
    Returns
    -------
    object
    See Also
    --------
    item2string
    """
    if string[0] == '\'' and string[-1] == '\'':
        out = string[1:-1]
    else:
        split = string.split(sep)
        if split[0][0:2] == '[[':  # case of multidimensional arrays
            out = string2array(sep.join(split))
        else:
            split = [i.strip() for i in split]  # remove dumb things
            split = [i if i is not '' else 'None' for i in split]  # handle empties
            # handle lists
            is_list = False
            list_chars = ['[', ']']
            for item_index, item_string in enumerate(split):
                if item_string == '[]':
                    continue
                if item_string[0] == '\'' and item_string[-1] == '\'':  # this is a string
                    continue
                for char in item_string:
                    if char in list_chars:
                        is_list = True
                for char in list_chars:
                    item_string = split[item_index]
                    split[item_index] = item_string.replace(char, '')
            # eval contents
            split = [i.strip() for i in split]  # remove dumb things
            split = [ast.literal_eval(i) for i in split]
            if len(split) == 1 and not is_list:
                split = split[0]
            out = split
    return out
