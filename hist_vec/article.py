

import ujson
import nltk.data
import spacy


class Article:

    nlp = spacy.load('en')

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
        doc = self.nlp(self.data['text'] or '')

        for sent in doc.sents:

            tokens = doc[sent.start:sent.end]

            # Convert to lowercase string.
            tokens = map(str, tokens)
            tokens = map(str.lower, tokens)

            yield list(tokens)
