"""Used for TXT file read and parse the data."""
from typing import List
import subprocess
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """TXTIngestor Strategy Class for txt file read and data parse."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Read the file and parse the data.

        Arguments:
            path {str} -- path where the txt file exists.
        """
        if not cls.can_ingest(path):
            raise Exception(f'Problem ingesting .txt file.'
                f'Please check for correct format/corrupt file.')

        file_ref = open(path, "r", encoding="utf-8-sig")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                new_Quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_Quote)

        file_ref.close()
        return quotes
