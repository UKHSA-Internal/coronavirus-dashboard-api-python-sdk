#!/usr/bin python3

"""
Coronavirus Dashboard API: Python SDK
=====================================

This is a Python SDK for the COVID-19 API, as published by
Public Health England on `Coronavirus (COVID-19) in the UK`_
dashboard.

The endpoint for the data provided using this SDK is:

    https://api.coronavirus.data.gov.uk/v1/data

.. _`Coronavirus (COVID-19) in the UK`: http://coronavirus.data.gov.uk/
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:

# 3rd party:

# Internal:
from uk_covid19.api_interface import Cov19API

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Header
__author__ = "Pouria Hadjibagheri"
__copyright__ = "Copyright (c) 2020, Public Health England"
__description__ = "SDK for the COVID-19 API (Coronavirus Dashboard in the UK)"
__license__ = "MIT"
__version__ = "1.2.2"
__url__ = "https://coronavirus.data.gov.uk/"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    "Cov19API"
]
