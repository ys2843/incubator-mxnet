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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sys, os, re, subprocess
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------
project = u'Apache MXNet'
author = u'%s developers' % project
copyright = u'2015-2019, %s' % author
github_doc_root = 'https://github.com/apache/incubator-mxnet/tree/master/docs/'
doc_root = 'https://mxnet.apache.org/'

# -- General configuration ---------------------------------------------------
# add markdown parser
source_parsers = {
    '.md': CommonMarkParser,
}
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'mxtheme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'primary_color': 'blue',
    'accent_color': 'deep_orange',
    'show_footer': True,
    'relative_url': os.environ.get('SPHINX_RELATIVE_URL', '/')
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../python_docs/themes/mx-theme']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../python_docs/_static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '../python_docs/_static/mxnet_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '../python_docs/_static/mxnet-icon.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../python_docs/_static']

html_css_files = [
    'mxnet.css',
]

html_js_files = [
    'autodoc.js'
]

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
  '**': 'relations.html'
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'formatdoc'

nbsphinx_execute = 'never'

# let the source file format to be xxx.ipynb instead of xxx.ipynb.txt
html_sourcelink_suffix = ''

def setup(app):
    app.add_transform(AutoStructify)
    app.add_config_value('recommonmark_config', {
    }, True)
    app.add_javascript('google_analytics.js')
    # import mxtheme
    # app.add_directive('card', mxtheme.CardDirective)