"""
Aragog
======

A collection of URL routers for Python.
"""
from setuptools import Command, setup

import aragog


class lint(Command):
    """
    Run python linting commands: pep8 & pyflakes on source tree
    """
    description = "Lint source code with python linters"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def pep8(self):
        from pep8 import StyleGuide

        sg = StyleGuide()
        sg.input_dir('aragog')

    def run(self):
        self.pep8()

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
    cmdclass={'lint': lint},
)
