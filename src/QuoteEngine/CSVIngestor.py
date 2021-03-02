"""Used for CSV file read and parse the data."""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSVIngestor Strategy Class for csv file read and data parse."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Read the file and parse the data.

        Arguments:
            path {str} -- path where the csv file exists.
        """
        if not cls.can_ingest(path):
            raise Exception(f'Problem ingesting .csv file.'
                            f'Please check for correct format/corrupt file.')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_Quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_Quote)

        return quotes