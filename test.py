import os
import sys
import platform

here = os.path.dirname(__file__)


__version__ = "Undefined"
with open("fuzzyset/__init__.py") as fh:
    for line in fh:
        if line.startswith("__version__"):
            exec(line.strip())

print(__version__)
