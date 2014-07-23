"""
Aragog
======

A collection of URL routers for Python.
"""
from setuptools import setup

import aragog

setup(
    name="aragog",
    description="A collection of python URL routers.",
    url="https://github.com/bramwelt/aragog",
    version=".".join(aragog.__version__),
    author="Trevor Bramwell",
    author_email="trevor@bramwell.net",
    packages=['aragog'],
    license="Apache2",
    install_requires=[],
    long_description=open("README.rst").read(),
    test_suite="test",
)
