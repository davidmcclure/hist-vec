

import ujson
import re


class BPOArticle:

    @classmethod
    def from_path(cls, path):
        """Hydrate from a path.
        """
        with open(path) as fh:
            return cls(ujson.load(fh))

    def __init__(self, data):
        """Wrap BPO article JSON.

        Args:
            data (dict)
        """
        self.data = data

    def sentences(self):
        """Split text into sentences.

        Yields: list of str
        """
        # Don't ask.
        sents = re.split(
            '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',
            self.data['text'] or ''
        )

        for sent in sents:
            yield re.findall('[a-z]+', sent.lower())
