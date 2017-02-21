

from .corpus import Corpus


class Models:

    def __init__(self, corpus_path, models_path):
        """Set corpus and models dirs.

        Args:
            corpus_path (str): Corpus root dir.
            models_path (str): Model root dir.
        """
        self.path = models_path

        self.corpus = Corpus(corpus_path)

    def train_word2vec(self, slice_name):
        """Given a slice name, train word2vec and save the model.

        Args:
            slice_name (str): 1880, 1900, etc.
        """
        pass
