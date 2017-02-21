

import ujson


class Article:

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
