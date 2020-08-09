# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from os import path
import sys
from datetime import datetime

doc_paths = path.dirname(path.abspath(__file__))
package_dir = path.abspath(path.join(doc_paths, path.pardir, path.pardir))

sys.path.insert(0, package_dir)

from uk_covid19 import __version__ as release


# -- Project information -----------------------------------------------------

project = 'uk-covid19'
copyright = '{:%Y} - Public Health England'.format(datetime.now())
author = 'Pouria Hadjibagheri'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

master_doc = 'index'
templates_path = ['_templates']
html_theme_path = ['_themes']
html_static_path = ['_static']
source_suffix = '.rst'
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

build_dir = path.abspath(path.join(doc_paths, path.pardir, "build"))

with open(path.join(build_dir, "version"), "w") as file:
    print(release, file=file)
