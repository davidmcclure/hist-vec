

import os


class Corpus:

    def __init__(self, path):
        """Wrap BPO slices corpus.

        Args:
            path (str): Corpus root.
        """
        self.path = path

    def slice_names(self):
        """Get a list of all slice names.
        """
        return next(os.walk(self.path))[1]
