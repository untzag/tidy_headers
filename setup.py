#! /usr/bin/env python


# --- import -------------------------------------------------------------------------------------


import os
from setuptools import setup, find_packages


# --- define -------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))


extra_files = []
extra_files.append(os.path.join(here, 'LICENSE'))
extra_files.append(os.path.join(here, 'README.md'))
extra_files.append(os.path.join(here, 'requirements.txt'))
extra_files.append(os.path.join(here, 'VERSION'))


# --- functions ----------------------------------------------------------------------------------


with open(os.path.join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()


with open(os.path.join(here, 'VERSION')) as version_file:
    version = version_file.read().strip()


# --- setup --------------------------------------------------------------------------------------


setup(
    name='tidy_headers',
    packages=find_packages(),
    package_data={'': extra_files},
    setup_requires=['pytest-runner'],
    install_requires=required,
    tests_require=['pytest', 'pytest-cov'],
    version=version,
    description='Easy headers, inspired by the tidy data formats.',
    author='Blaise Thompson',
    author_email='blaise@untzag.com',
    license='MIT',
    url='https://github.com/untzag/tidy_headers',
    keywords='metadata file format',
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Intended Audience :: Science/Research',
                 'Topic :: Utilities',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5']
)
