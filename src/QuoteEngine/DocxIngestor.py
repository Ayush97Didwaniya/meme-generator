"""Used for doc file read and parse the data."""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """DocxIngestor Strategy Class for doc file read and data parse."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Read the file and parse the data.

        Arguments:
            path {str} -- path where the doc file exists.
        """
        if not cls.can_ingest(path):
            raise Exception(f'Problem ingesting .docx file.'
                f'Please check for correct format/corrupt file.')
            
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split(' - ')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        return quotes