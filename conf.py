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
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'User\'s Guide'
copyright = '2021, AIMMS B.V.'
author = 'AIMMS'

book_title = "User\'s Guide"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx_aimms_theme',
'sphinx.ext.mathjax',
'sphinx.ext.intersphinx',
'sphinx.builders.linkcheck',
'sphinxcontrib.bibtex',      
]

if os.name != 'nt':

    #Imports sitemap extension to build the sitemap automatically
    extensions.append('sphinx_sitemap')
    html_baseurl = "https://documentation.aimms.com/user-guide/"
    extensions.append('sphinx_last_updated_by_git')

intersphinx_mapping = {'fr': ('https://documentation.aimms.com/functionreference/',
                                  (None,'objects-functionreference.inv')),
                        'lr': ('https://documentation.aimms.com/language-reference/', None),
                        'howto': ('https://how-to.aimms.com/', None),
                        'doc': ('https://documentation.aimms.com/', None),}
html_theme = 'sphinx_aimms_theme'

bibtex_bibfiles = ['bibbase.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

if os.name == 'nt':
   
   Display_edit_on_gitlab = True
   # if builds locally (a windows machine), do not displays external extensions (Google Analytics, Community Embeddable, Algolia search, etc.)
   Display_3rd_Party_Extensions = False
else:

   # if builds on GitLab (a Linux machine), force "Edit on Gitlab" not to be shown, and displays external extensions (Google Analytics, Community Embeddable, Algolia search, etc.)
   Display_edit_on_gitlab = False
   Display_3rd_Party_Extensions = True


html_theme_options = {

    'doc_title' : 'User\'s Guide',
    'home_page_title': 'AIMMS User\'s Guide',
    'home_page_description': "Creating and Managing a Model, Data management, External calls to AIMMS",
    'display_community_embeddable' : Display_3rd_Party_Extensions,
    'display_local_toc' : True,
    'google_analytics_id': 'UA-1290545-13',
    'generate_google_analytics' : Display_3rd_Party_Extensions,
    'display_algolia_search' : Display_3rd_Party_Extensions,
    'algolia_appid': 'BH4D9OD16A', 
    'algolia_appkey': 'f7e44f5b57ababa5c5ceb1e1087ae3b1', 
    'algolia_indexname': 'aimms',
    'display_help_and_feedback' : False,

}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'pdflatex'

my_preamble =  '''
\\usepackage{etoolbox}
\\BeforeBeginEnvironment{fulllineitems}{\\begingroup\\color{white}\\tiny}%
\\AfterEndEnvironment{fulllineitems}{\\endgroup}%
'''

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    #'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': my_preamble,
    #changes color of internal hyperlinks
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
    'sphinxsetup': 'InnerLinkColor={RGB}{203,65,84}, OuterLinkColor={RGB}{0,102,204}',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_doc_name = 'AIMMS_user.tex'

latex_documents = [
    (master_doc, latex_doc_name, book_title,
     u'AIMMS', 'manual', True),
]

latex_logo = "AIMMS_logo_BlackWhite-PRINT-900x508.jpg"

latex_show_pagerefs = True


numfig = True
