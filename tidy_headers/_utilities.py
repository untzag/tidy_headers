"""Utilities."""


# --- import -------------------------------------------------------------------------------------


# --- functions ----------------------------------------------------------------------------------


def flatten_list(items, seqtypes=(list, tuple), in_place=True):
    """Flatten an irregular sequence.

    Works generally but may be slower than it could be if you can make
    assumptions about your list.

    `Source`__

    __ https://stackoverflow.com/a/10824086

    Parameters
    ----------
    items : iterable
        The irregular sequence to flatten.
    seqtypes : iterable of types (optional)
        Types to flatten. Default is (list, tuple).
    in_place : boolean (optional)
        Toggle in_place flattening. Default is True.

    Returns
    -------
    list
        Flattened list.

    Examples
    --------
    >>> l = [[[1, 2, 3], [4, 5]], 6]
    >>> flatten_list(l)
    [1, 2, 3, 4, 5, 6]
    """
    if not in_place:
        items = items[:]
    for i, _ in enumerate(items):
        while i < len(items) and isinstance(items[i], seqtypes):
            items[i:i + 1] = items[i]
    return items
