#!/usr/bin/env python3
import os
import sys
import site
import setuptools
from distutils.core import setup


# Editable install in user site directory can be allowed with this hack:
# https://github.com/pypa/pip/issues/7953.
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

setup(
    name="ETEC325Library",
    version="2.0.0",
    description="Library functions for ETEC 325",
    author="ETEC 325",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "scipy",
        "matplotlib",
        "openpyxl",
        "pandas",
        "scikit-learn",
        "XlsxWriter",
        "wespeaker",
        "numpy"
    ],
    python_requires=">=3.9",
)
