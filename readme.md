# Einführung ins TrampolinTurnen

[![Pages-Deployment](https://github.com/orgua/TrampolinTurnen/actions/workflows/sphinx_to_pages.yaml/badge.svg)](https://github.com/orgua/TrampolinTurnen/actions/workflows/sphinx_to_pages.yaml)

**Inhalt als Webseite 📱**: <https://orgua.github.io/TrampolinTurnen/>

**Inhalt als PDF 📄**: <https://github.com/orgua/TrampolinTurnen/releases>

**Inhalt als reStructuredText 💻**: <https://github.com/orgua/TrampolinTurnen/tree/main/docs/content>

---

Dieses Repository enthält die Quellen zum Leitfaden für Trainer,Kursleiter, Lehrer und Gruppenhelfer.
Es wird daran gearbeitet die Basisscheine I und II, sowie Teile von der Trainer C Ausbildung abzudecken.
Die Inhalte werden sowohl als PDFBroschüre, als auch als Webseite veröffentlicht.

## Wie kann ich beitragen?

Schreibfehler gefunden?
Bessere Methodik zu bieten?
Hilfe und Anmerkungen sind willkommen.
Die Quellen befinden sich unter `docs/content` in Form von reStructuredText-Dateien.

- [Writing reStructuredText](https://www.writethedocs.org/guide/writing/reStructuredText/)

## Basic Installation for Web-Content

Compiling this document needs a shell.

The dev-environment is handled by uv, follow [their instructions](https://docs.astral.sh/uv/getting-started/installation/) for installation.
It will install all dependencies, including python if needed, into a local virtual environment.

For installation:

- clone repository
- navigate shell into directory
- install environment
- activate shell (`uv` will tell you how)

```Shell
git clone https://github.com/orgua/TrampolinTurnen

cd TrampolinTurnen

uv venv
```

Compiling the document:

```Shell
cd docs
sphinx-build -b html ./ _build/html
# or ?
make html
```

Viewing the document in a browser:

```Shell
cd _build/html
python3 -m http.server
```

In browser go to [localhost:8000](localhost:8000) to view the documentation.

## Generating a PDF (+Install)

Install for Ubuntu / Debian, following [Sphinx.LaTeXBuilder](https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder)

```Shell
sudo apt install texlive-latex-recommended
sudo apt install texlive-fonts-recommended
sudo apt install texlive-latex-extra
sudo apt install tex-gyre latexmk
sudo apt install texlive-lang-german
```

Generating the PDF

```Shell
cd docs/
# make latex
make latexpdf
```

## Generating a DocX (+Install)

[Pandoc](https://pandoc.org/) must be installed, then simply run `.\rst2docx.py`.

**Problems with Pandoc**

- internal links don't work ("Name <Link>")
- *leads* (small introduction into chapter) is not converted and still has "lead" in front
- same for "tip", "caution", "warning", and more?
- no TOC

-> could be solved with ``rstdoc``-lib, but that has other problems.

## Release-Procedure

- increase version number by executing ``bump2version`` (see cmds below)
- install and run ``pre-commit`` for QA-Checks, see steps below
- update changelog in ``CHANGELOG.md``
- move code from dev-branch to main by PR
- add tag to commit - reflecting current version number - i.e. ``v0.9.0``
  - GitHub automatically creates a release & pushes the release to pypi
- update release-text with latest Changelog (from `CHANGELOG.md`)
- rebase dev-branch

```Shell
bump2version --allow-dirty --new-version 0.8.15 patch

pre-commit run --all-files
```

## TODO

- switch to markdown / myst-parser
- neutrale Anrede konsequenter umsetzen
- Einsatz von Klammern reduzieren -> Nebensätze
- Grundpositionen den Grundsprüngen vorlargern
  - Breitenachsenrotation vw rw
  - schraube
  - vorgespannte, s-form
  - c-plus, c-minus
- Jeder Sprung mit festem Schema
  - Einleitung
  - Leistungsvoraussetzungen
  - Bewegungsbeschreibung
  - Methodik
  - Fehler und Korrekturen
  - Hilfestellung
- Texte in kleinere Abschnitte teilen - um später kompakte Übersichten zu generieren (Aufbau, Hilfestellungen, Fehlerbilder, )
- add videos
    - basics techniques
