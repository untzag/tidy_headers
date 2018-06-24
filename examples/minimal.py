"""Minimum example of tidy headers."""


# --- import -------------------------------------------------------------------------------------


import os
import time
import collections

import numpy as np

import tidy_headers


# --- define -------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))


# --- workspace ----------------------------------------------------------------------------------


filepath = os.path.join(here, "minimal.txt")

# create metadata
meta = collections.OrderedDict()
meta["time"] = time.time()
meta["name"] = "Blaise Thompson"
meta["colors"] = ["red", "blue", "green", "white"]
meta["number"] = 42
meta["array"] = np.random.random((5, 3))

# write metadata
tidy_headers.write(filepath, meta)

# read metadata
print(tidy_headers.read(filepath))
