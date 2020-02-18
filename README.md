# paperfinder

Given a URL to a paper on a publisher's website, find its DOI and a BibTex
citation. Output can be given as plain text or JSON.

This takes some of the pain out of dealing with publishers' websites. Of
course, it is possible to pair this tool with SciHub to get the actual PDF (go
to `https://sci-hub.se/<DOI>`, but I could not possibly endorse piracy in this
way...

E.g:

```
$ pf "https://www.sciencedirect.com/science/article/pii/000437029400041X"
DOI: 10.1016/0004-3702(94)00041-X

BibTeX:
@article{Dung_1995,
        doi = {10.1016/0004-3702(94)00041-x},
        url = {https://doi.org/10.1016%2F0004-3702%2894%2900041-x},
        year = 1995,
        month = {sep},
        publisher = {Elsevier {BV}},
        volume = {77},
        number = {2},
        pages = {321--357},
        author = {Phan Minh Dung},
        title = {On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games},
        journal = {Artificial Intelligence}
}
```

```
$ pf --format json "https://www.sciencedirect.com/science/article/pii/
000437029400041X"
{
  "doi": "10.1016/0004-3702(94)00041-X",
  "bib": "@article{Dung_1995,\n\tdoi = {10.1016/0004-3702(94)00041-x},\n\turl = {https://doi.org/10.1016%2F0004-3702%2894%2900041-x},\n\tyear = 1995,\n\tmonth = {sep},\n\tpublisher = {Elsevier {BV}},\n\tvolume = {77},\n\tnumber = {2},\n\tpages = {321--357},\n\tauthor = {Phan Minh Dung},\n\ttitle = {On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games},\n\tjournal = {Artificial Intelligence}\n}"
}
```

Note that `pf` works for a [very small number of
publishers](#supported-publishers), and may break if publisher web pages or
URLs change.

## Installation

```
$ git clone https://github.com/joesingo/paperfinder
$ cd paperfinder
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install .
```

## Usage

```
Usage: pf [OPTIONS] URL

  Given a URL to a paper on a publisher's website, find its DOI and a BibTex
  citation

Options:
  -f, --format [text|json]
  --help                    Show this message and exit.
```

## Supported publishers

- ScienceDirect
- Springer

This list should grow over time as I use the tool more.

