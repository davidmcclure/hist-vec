

import ujson
import nltk.data


class Article:

    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

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
        """
        text = self.data['text'] or ''
        return self.sent_detector.tokenize(text)
