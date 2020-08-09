#!/usr/bin python3

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
from enum import Enum, auto

# 3rd party:

# Internal: 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'DataFormat'
]


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class DataFormat(AutoName):
    JSON = auto()
    XML = auto()
    CSV = auto()
