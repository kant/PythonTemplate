#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# {{ cookiecutter.project_slug }} documentation build configuration file, created by
# sphinx-quickstart on Tue Dec 19 17:02:44 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import subprocess
import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

working_dir = os.path.abspath(os.path.dirname(__file__))
root_dir_rel = os.path.join('..')
root_dir_abs = os.path.abspath(root_dir_rel)
module_path = root_dir_abs
sys.path.insert(0, module_path)
logo_file = 'project-icon.png'
logo_path = os.path.join('..', logo_file)

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    'tests',
    'run_*',
    'setup.py',
    '_build',
    'Thumbs.db',
    '.DS_Store',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
static_folder = 'static'
html_static_path = [static_folder]


def generate_apidocs(*args):
    """Generate API docs automatically by trawling the available modules"""

    global working_dir, module_path
    output_path = working_dir
    apidoc_command_path = 'sphinx-apidoc'
    if hasattr(sys, 'real_prefix'):  # called from a virtualenv
        apidoc_command_path = os.path.join(sys.prefix, 'bin', 'sphinx-apidoc')
        apidoc_command_path = os.path.abspath(apidoc_command_path)
    subprocess.check_call(
        [apidoc_command_path, '--force', '--separate'] +
        ['-o', output_path, module_path] +
        [os.path.join(root_dir_abs, pattern) for pattern in exclude_patterns])


def setup(app):
    # Hook to allow for automatic generation of API docs
    # before doc deployment begins.
    app.connect('builder-inited', generate_apidocs)


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.imgmath']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'


# This allows modules to be indexed under the submodule name rather than all appearing under {{ cookiecutter.pkg_name }}
modindex_common_prefix = [
    '{{ cookiecutter.pkg_name }}.'
]

# General information about the project.
project = u'{{ cookiecutter.project_name }}'
copyright = u"{% now 'local', '%Y' %}, University College London"
author = u'{{ cookiecutter.full_name }}'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The short X.Y version.
# version = {{ cookiecutter.pkg_name }}.__version__
# The full version, including alpha/beta/rc tags.
# release = {{ cookiecutter.pkg_name }}.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'classic'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
doc_black = '#0A0A0A'
doc_red = '#E03C31'
doc_gray = '#979999'
doc_blue = '#00627D'
doc_dark_red = '#C53B2C'
doc_white = '#FEFEFE'
html_theme_options = {
    'footerbgcolor': doc_gray,
    'footertextcolor': doc_black,
    'sidebarbgcolor': doc_white,
    'sidebartextcolor': doc_black,
    'sidebarlinkcolor': doc_red,
    'relbarbgcolor': doc_white,
    'relbartextcolor': doc_black,
    'relbarlinkcolor': doc_red,
    'bgcolor': doc_white,
    'textcolor': doc_black,
    'linkcolor': doc_red,
    'visitedlinkcolor': doc_dark_red,
    'headbgcolor': doc_white,
    'headtextcolor': doc_black,
    'headlinkcolor': doc_red,
    'codebgcolor': doc_blue,
    'codetextcolor': doc_black,
    'stickysidebar': 'true',
}

html_logo = logo_path

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = '{{ cookiecutter.project_slug }}doc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', '{{ cookiecutter.project_slug }}.tex',
     u'{{ cookiecutter.project_name }} Documentation',
     u'{{ cookiecutter.full_name }}', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', '{{ cookiecutter.project_slug }}',
     u'{{ cookiecutter.project_name }} Documentation',
     [u'{{ cookiecutter.full_name }}'], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', '{{ cookiecutter.project_slug }}',
     u'{{ cookiecutter.project_name }} Documentation',
     u'{{ cookiecutter.full_name }}',
     '{{ cookiecutter.project_slug }}',
     'One line description of project.',
     'Miscellaneous'),
]



