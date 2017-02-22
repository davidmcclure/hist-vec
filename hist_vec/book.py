

from bs4 import BeautifulSoup


class Book:

    @classmethod
    def from_path(cls, path):
        """Make an instance from an XML file.

        Args:
            path (str)
        """
        with open(path, 'rb') as fh:
            return cls(fh.read())

    def __init__(self, xml):
        """Parse the XML tree.

        Args:
            xml (str)
        """
        self.tree = BeautifulSoup(xml, 'xml')

    def plain_text(self):
        """Return raw text string.

        Returns: str
        """
        ps = self.tree.select('p')

        return ' '.join([list(p.stripped_strings)[0] for p in ps])
