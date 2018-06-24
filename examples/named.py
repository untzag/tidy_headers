"""tidy_headers works great as a way to store column names."""


# --- import -------------------------------------------------------------------------------------


import os
import time
import collections

import numpy as np

import tidy_headers


# --- define -------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))


# --- workspace ----------------------------------------------------------------------------------


filepath = os.path.join(here, "named.txt")


# make data
meta = collections.OrderedDict()
meta["time"] = time.time()
meta["name"] = ["index", "apples", "oranges"]
index = np.arange(21)
apples = np.random.randint(0, 99, 21)
oranges = np.random.randint(0, 99, 21)


# write
tidy_headers.write(filepath, meta)
with open(filepath, "ab") as f:
    np.savetxt(f, np.vstack([index, apples, oranges]).T, fmt="%i", delimiter="\t")
