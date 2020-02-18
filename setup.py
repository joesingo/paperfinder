"""
Adapted from https://github.com/pypa/sampleproject
"""
from os import path

from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

with open(path.join(HERE, "requirements.txt"), encoding="utf-8") as f:
    REQUIREMENTS = f.read().split("\n")

setup(
    name="paperfinder",
    version="0.0.1",
    description=("Simple tool to output the DOI and BibTeX for a paper given "
                 "its URL on the publisher's website")
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/joesingo/paperfinder",
    author="Joe Singleton",
    author_email="joesingo@gmail.com",
    packages=find_packages(exclude=["contrib", "doc", "tests"]),
    python_requires=">=3.5",
    install_requires=REQUIREMENTS,
    entry_points={
        "console_scripts": [
            "pf=paperfinder.client:main"
        ]
    }
)
