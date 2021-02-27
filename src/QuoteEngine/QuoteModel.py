"""Quote Model."""


class QuoteModel():
    """Quote Model Class."""

    def __init__(self, body, authorName):
        """Create a new Quote.

        Arguments:
            body {str} -- the body of the Quote
            authorName {str} -- the author name of the Quote
        """
        self.body = body
        self.author = authorName

    def __repr__(self):
        """Return Quote with author name."""
        return f'<"{self.body}" - {self.author}>'
