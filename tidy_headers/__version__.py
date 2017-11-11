"""Define tidy_headers version."""


# --- import --------------------------------------------------------------------------------------


import os


# ---- define -------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))


__all__ = ['__version__']


# --- version -------------------------------------------------------------------------------------


# read from VERSION file
with open(os.path.join(os.path.dirname(here), 'VERSION')) as f:
    __version__ = f.read().strip()
