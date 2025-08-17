# import os
# import sys
# sys.path.insert(0, os.path.abspath(".."))

# project = "Hybrid Framework"
# author = "Your Team"
# release = "0.1"

# extensions = [
#     "sphinx.ext.autodoc",        # Auto-generate API docs from docstrings
#     "sphinx.ext.napoleon",       # Google/NumPy style docstrings
#     "sphinx.ext.viewcode",       # Link to source code
#     "sphinx_autodoc_typehints",  # Type hints in docs
#     "m2r2",                      # Parse Markdown
# ]

# source_suffix = [".rst", ".md"]
# html_theme = "sphinx_rtd_theme"


import os
import sys
sys.path.insert(0, os.path.abspath(".."))

project = "Hybrid Framework"
author = "Your Team"
release = "0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",   # for Google/NumPy style docstrings
    "sphinx.ext.viewcode",
    "myst_parser",           # allow markdown in docs
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"


