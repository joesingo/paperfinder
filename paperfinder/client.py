import json
import sys
from typing import Optional

from bs4 import BeautifulSoup
import click
import requests

class PaperFinderError(Exception):
    """
    Application specific error
    """

class Publisher:
    PREFIX: Optional[str] = None

    @classmethod
    def url_matches(cls, url: str) -> bool:
        assert isinstance(cls.PREFIX, str)
        return url.startswith(cls.PREFIX)

    def get_doi(self, url: str) -> str:
        raise NotImplementedError

class Springer(Publisher):
    PREFIX = "https://link.springer.com/chapter/"

    def get_doi(self, url: str) -> str:
        return url[len(self.PREFIX):]

class ScienceDirect(Publisher):
    PREFIX = "https://www.sciencedirect.com/"

    def get_doi(self, url: str) -> str:
        user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.106 Safari/537.36")
        resp = requests.get(url, headers={"User-Agent": user_agent})
        doc = BeautifulSoup(resp.content, features="html.parser")
        meta = doc.find("meta", attrs={"name": "citation_doi"})
        if not meta:
            raise PaperFinderError("could not find 'citation_doi' <meta> tag")
        try:
            return meta["content"]
        except KeyError:
            raise PaperFinderError("DOI <meta> tag does not have 'content' attribute")


def get_publisher(url: str) -> Publisher:
    classes = Publisher.__subclasses__()
    for cls in classes:
        if cls.url_matches(url):
            return cls()
    raise PaperFinderError(
        f"could not find a matching publisher for URL '{url}'"
    )

def get_bibtex(doi: str) -> str:
    base = "https://doi.org/"
    doi_url = f"{base}/{doi}"
    headers = {"Accept": "application/x-bibtex; charset=utf-8"}
    resp = requests.get(doi_url, headers=headers, allow_redirects=True)
    if resp.status_code != 200:
        raise PaperFinderError("could not obtain BibTeX citation")
    return resp.text

@click.command()
@click.argument("url")
@click.option("--format", "-f", "fmt", type=click.Choice(["text", "json"]), default="text")
def main(url: str, fmt: str):
    """
    Given a URL to a paper on a publisher's website, find its DOI and a BibTex
    citation
    """
    try:
        pub: Publisher = get_publisher(url)
        doi = pub.get_doi(url)
        bibtex = get_bibtex(doi)
    except PaperFinderError as ex:
        print(f"{sys.arv[0]}: {ex}", file=sys.stderr)
        return 1

    if fmt == "text":
        print(f"DOI: {doi}")
        print("")
        print(f"BibTeX:\n{bibtex}")
    elif fmt == "json":
        obj = {"doi": doi, "bib": bibtex}
        print(json.dumps(obj, indent=2))
