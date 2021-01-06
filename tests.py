# --- import -------------------------------------------------------------------------------------


import tempfile

import numpy as np

import tidy_headers


# --- helpers ------------------------------------------------------------------------------------


def assert_dict_equal(a, b):
    assert len(a.keys()) == len(b.keys())
    for key, value in a.items():
        if hasattr(value, "dtype"):
            assert np.asarray(b[key]).all() == np.array(value).all()
        else:
            assert b[key] == value


# --- test ---------------------------------------------------------------------------------------


def test_float():
    f = tempfile.NamedTemporaryFile()
    d = {"zero": 0.0, "four": 4.0, "large": 124.0, "negative": -12.0, "fraction": 0.5}
    tidy_headers.write(f.name, d)
    assert_dict_equal(d, tidy_headers.read(f.name))
    f.close()


def test_int():
    f = tempfile.NamedTemporaryFile()
    d = {"zero": 0, "four": 4, "large": 1200000, "negative": -1}
    tidy_headers.write(f.name, d)
    assert_dict_equal(d, tidy_headers.read(f.name))
    f.close()


def test_list():
    f = tempfile.NamedTemporaryFile()
    d = {}
    d["hello"] = ["a", "b", "c", "d"]
    d["blaise"] = [0, 1, 2, 3, 4, 5, 6, -124]
    d["mixture"] = ["blaise", "wisconsin", "echo", "wisconsin"]
    tidy_headers.write(f.name, d)
    assert_dict_equal(d, tidy_headers.read(f.name))
    f.close()


def test_array():
    f = tempfile.NamedTemporaryFile()
    d = {}
    d["5"] = np.random.random(5)
    d["12, 45"] = np.random.random((12, 45))
    d["7, 15, 2"] = np.random.random((7, 15, 2))
    tidy_headers.write(f.name, d)
    assert_dict_equal(d, tidy_headers.read(f.name))
    f.close()


def test_str():
    f = tempfile.NamedTemporaryFile()
    d = {"blaise": "thompson", "red": "tomato", "love": "hate", "madison": "wisconsin"}
    tidy_headers.write(f.name, d)
    assert_dict_equal(d, tidy_headers.read(f.name))
    f.close()


def test_array_nans():
    f = tempfile.NamedTemporaryFile()
    d = {}
    d["nan"] = np.array([np.nan])
    d["inf"] = np.array([np.inf])
    d["-inf"] = np.array([-np.inf])
    tidy_headers.write(f.name, d)
    assert_dict_equal(d, tidy_headers.read(f.name))
    f.close()
