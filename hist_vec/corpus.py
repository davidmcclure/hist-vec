

import os

from .utils import scan_paths
from .article import Article


class Corpus:

    def __init__(self, path):
        """Wrap BPO slices corpus.

        Args:
            path (str): Corpus root.
        """
        self.path = path

    def slice_names(self):
        """Get a list of all slice names.

        Returns: list of str
        """
        return next(os.walk(self.path))[1]

    def sentences(self, slice_name):
        """Get a list of all sentences for a slice.

        Yields: str
        """
        slice_path = os.path.join(self.path, slice_name)

        for path in scan_paths(slice_path):
            article = Article.from_path(path)
            yield from article.sentences()
