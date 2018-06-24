"""Define tidy_headers version."""

import os

here = os.path.abspath(os.path.dirname(__file__))

__all__ = ["__version__"]

# read from VERSION file
with open(os.path.join(here, "VERSION")) as f:
    __version__ = f.read().strip()
