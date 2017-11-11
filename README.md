# tidy_headers

`tidy_headers` stores metadata in beautifully readable plain text headers.

## example

For some `filepath`, 

```python
import collections
import tidy_headers
meta = collections.OrderedDict()
meta['date'] = '2017-11-10'
meta['location'] = 'Madison, Wisconsin, USA'
meta['name'] = ['batch', 'apples', 'pineapple', 'oregano', 'tomatoes']
tidy_headers.write(filepath, meta)
```

To get the dictionary back, simply `read`:

```python
meta = tidy_headers.read(filepath)
```

:tada:

See the examples directory for more.

## installation

### using pip

```
pip install tidy_headers
```

### using conda

```
conda config --add channels conda-forge
conda install tidy_headers
```

## allowed values

`tidy_headers` strives to write plain text headers in an unambiguous way such that an identical metadata dictionary can be generated using `read`. This process is only reliable for the following subset of python types:

- `str`
- `int`
- `float`
- `list` containing any combination of the above
- `numpy.ndarray` (arbitrary size and dimensionality)

Metadata dictionaries containing only these types are guaranteed to `read` and `write` succesfully.
