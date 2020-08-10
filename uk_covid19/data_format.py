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
    def _generate_next_value_(self, start, count, last_values):
        return self.lower()


class DataFormat(AutoName):
    """
    Formats of the API Response.

    .. versionadded:: 1.2.0
    """
    JSON = auto()
    XML = auto()
    CSV = auto()
