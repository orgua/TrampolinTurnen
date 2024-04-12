"""
A script that feeds the sphinx-rst-content into pandoc and generates a complete DocX

Note: pandoc must be installed via apt

pre-tests with other tools:

rstdoc  index.rst test.docx docx
rstdoc ./doc test.docx docx
rstdcx -I docs docs/index.rst test.docx docx
rstdcx --rest ./doco --rstrest

pandoc -o test.docx docs/index.rst

Things to also try with pandoc:

--file-scope
--toc
--toc-depth
--reference-doc=

"""

import os
from pathlib import Path

file_path = Path(__file__) / "docs/content"
temp_path = Path(__file__) / "docs/_build"

files = [
    "einleitung",
    "pflichten",
    "sicherheit",
    "gymnastik",
    "tuchgewoehnung",
    "spiele",
    "grundspruenge",
    "sprungverbindung",
    "materialien",
]

content = []
with (temp_path / "content.rst").open("w", encoding="utf-8") as fw:
    fw.seek(0)
    fw.truncate()

    for file in files:
        fw.write("\n\n")
        with (file_path / (file + ".rst")).open(encoding="utf-8") as fd:
            content = fd.read()
            fw.write(content)


os.chdir(temp_path)
os.system("pandoc -o content_pandoc.docx content.rst")
# os.system(f"rstdoc content.rst content_rstdoc.docx docx")
# os.system(f"rstdcx content.rst content_rstdcx.docx docx")
# more secure:
# subprocess.run(["/path/pandoc", "-o", "content.docx", "content.rst"], timeout=60, check=False)
