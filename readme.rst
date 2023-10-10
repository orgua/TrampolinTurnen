Einführung ins TrampolinTurnen
==============================

.. image:: https://github.com/orgua/TrampolinTurnen/actions/workflows/pages/pages-build-deployment/badge.svg
    :target: https://github.com/orgua/TrampolinTurnen/actions/workflows/pages/pages-build-deployment
    :name: pages-deployment

Links:

- `Inhalt als Webseite 📱 <https://orgua.github.io/TrampolinTurnen/>`_

- `Inhalt als PDF 📄 <https://github.com/orgua/TrampolinTurnen/releases>`_

- `Inhalt als reStructuredText 💻 <https://github.com/orgua/TrampolinTurnen/tree/main/docs/content>`_

Latest Changes:

- 0.8.5

  - Anpassungen am build-system
  - kleinere Details am Skript überarbeitet

- 0.8.2

  - Kapitel 1-4 überarbeitet

- 0.8.0

  - Fehlerbilder der Grundsprünge erweitert
  - Phasendarstellungen hinzugefügt
  - Trampolinaufbauten hinzugefügt

- 0.7.5

  - viel Restrukturierungen des Inhalts
  - Grammatik und Rechtschreibprüfung verbessert
  - Füllwörter reduziert (viele unnötige "auch")
  - Mindestsatz an Aufgaben oder Ausführungen für Grobformen etabliert
  - neue Quellen eingearbeitet


Basic Installation for Web-Content
-----------------------------------

Compiling this document needs Python 3 and a shell.
For installation:

.. code-block:: bash

    git clone ....

    pip3 install pipenv
    # pip3 install --upgrade pip pipenv wheel setuptools

    pipenv install

    pipenv shell

Compiling the document:

.. code-block:: bash

    cd docs
    sphinx-build -b html ./ _build/html
    # or ?
    make html

Viewing the document in a browser:

.. code-block:: bash

    cd _build/html
    python3 -m http.server


In browser go to `<localhost:8000>`_ to view the documentation.

Generating a PDF (+Install)
---------------------------

Install for Ubuntu / Debian, following `Sphinx.LaTeXBuilder <https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder>`_

.. code-block:: bash

    sudo apt install texlive-latex-recommended
    sudo apt install texlive-fonts-recommended
    sudo apt install texlive-latex-extra
    sudo apt install tex-gyre latexmk
    sudo apt install texlive-lang-german

Generating the PDF

.. code-block:: bash

    cd docs/
    # make latex
    make latexpdf

Generating a DocX (+Install)
----------------------------

`Pandoc <https://pandoc.org/>`_ must be installed, then simply run ``.\rst2docx.py``.

**Problems with Pandoc**

- internal links don't work ("Name <Link>")
- *leads* (small introduction into chapter) is not converted and still has "lead" in front
- same for "tip", "caution", "warning", and more?
- no TOC

-> could be solved with ``rstdoc``-lib, but that has other problems.

Wie kann ich beitragen?
--------------------------------

Schreibfehler gefunden? Bessere Methodik zu bieten? Hilfe und Anmerkungen sind willkommen. Die Quellen befinden sich unter ``docs/content`` in Form von reStructuredText-Dateien.

- `Writing reStructuredText <https://www.writethedocs.org/guide/writing/reStructuredText/>`_

TODO
-------------

- switch to markdown / myst-parser
- add auto-releaser on tag
- Einsatz von Klammern reduzieren -> Nebensätze
- add videos

    - basics techniques
