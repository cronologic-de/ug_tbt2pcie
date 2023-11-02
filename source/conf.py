# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'User Guide Appendix – Desktop Solutions'
copyright = "CC BY-ND 4.0 DEED"
author = "cronologic GmbH & Co. KG"
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
]

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

rst_prolog = open("global.rst", "r").read()

templates_path = ["_templates"]
exclude_patterns = ["global.rst"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Customizing for PDF output ----------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    "fontpkg" : "",
    "preamble": r"""
        \usepackage[
            font=montserrat,
            sphinx,
            drawframe]
        {cronologic}
        \definecolor{ctypered}{RGB}{142,33,0} % C-type auto highlighting color
        \newcommand{\docutilsrolectypered}[1]{{\color{ctypered} #1}}
        \newcommand{\docutilsrolered}[1]{{\color{red} #1}}
        \newcommand{\docutilsrolecronoblue}[1]{{\color{cronblue} #1}}
    """,
    "extraclassoptions": r"openany",
    "tableofcontents":r"\tableofcontents",
    "maketitle": r"\includepdf[pages={1}]{titlepage.pdf}",
    # "sphinxsetup": r"""
    #     hmargin={1.5cm,1.5cm},
    #     vmargin={1.85cm,1.40cm}
    # """
}
latex_theme = "manual" # manual (book class) or howto (article class)
latex_additional_files = [
    "cronologic.sty",
    "extraplaceins.sty",
    "_figures/titlepage.pdf",
]

numfig = True
numfig_format = {
    "figure":"Figure %s:",
    "table":"Table %s:"
}
numfig_secnum_depth = 1