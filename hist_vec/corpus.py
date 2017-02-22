

import os

from gensim.models.word2vec import Word2Vec

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

        Args:
            slice_name (str)

        Yields: str
        """
        slice_path = os.path.join(self.path, slice_name)

        for path in scan_paths(slice_path):

            article = Article.from_path(path)

            yield from article.sentences()

    def word2vec_model(self, slice_name):
        """Train a word2vec model on slice.

        Args:
            slice_name (str)

        Returns: Word2Vec
        """
        sentences = list(self.sentences(slice_name))

        return Word2Vec(sentences, size=100, min_count=100, workers=8)
