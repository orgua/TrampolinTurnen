# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = "Trampolinturnen"
project_full = "Einführung ins Trampolinturnen"
project_copyright = "2022, Ingmar Splitt"
author = "Ingmar Splitt"
release = "0.8.1"
builder = "html latexpdf"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxawesome_theme",
    "sphinx_sitemap",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "de"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project_full
html_collapsible_definitions = True
html_copy_source = False

html_permalinks_icon = "<span>#</span>"
html_theme = "sphinxawesome_theme"
html_theme_options = {
    "show_scrolltop": True,
    "show_prev_next": True,
    "extra_header_links": {
        "PDF-Version": "https://github.com/orgua/TrampolinTurnen/releases",
        "Quelldateien": "https://github.com/orgua/TrampolinTurnen/tree/main/docs/content",
    },
}
# TODO: https://sphinxawesome.xyz/how-to/options/
html_baseurl = "https://orgua.github.io/TrampolinTurnen/"
html_extra_path = ["robots.txt"]
html_static_path = ["_static"]

sitemap_url_scheme = "{link}"

# -- Options for LATEX output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/latex.html
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-latex_theme


# latex_documents = [(
#     "index",  # startdocname
#     project,  # targetname
#     project_full,  # title
#     author,  # author
#     "report",  # theme
#     False,  # toctree_only
# )]

latex_theme = "manual"
# manual    sphinx-report - much wasted space
# howto     no page-break at all -> TODO: has latex_appendices?
# report    ok, but small

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    "fncychap": "",  # '\\usepackage[Bjornstrup]{fncychap}',
    "transition": "\\bigskip",
    # passoptionstopackages
    "preamble": r"\input{style.tex.txt}",
    # MTB
    "sphinxsetup": """
        InnerLinkColor = {rgb}{0.6,0,0}, % red
        OuterLinkColor = {rgb}{0.6,0,0},
        TitleColor = {rgb}{0.0,0,0}, % black
        marginpar = 0in, % no difference
    """,
}

latex_additional_files = ["style.tex.txt"]
