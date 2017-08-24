

import regex

from bs4 import BeautifulSoup


class Book:

    @classmethod
    def from_path(cls, path):
        """Make an instance from an XML file.

        Args:
            path (str)
        """
        with open(path, 'r') as fh:
            return cls(fh.read())

    def __init__(self, text):
        """Parse the XML tree.
        """
        self.text = text

    def sentences(self):
        """Split text into sentences.

        Yields: list of str
        """
        yield regex.findall('\p{L}+', self.text.lower())
