"""Used for PDF file read and parse the data."""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDFIngestor Strategy Class for pdf file read and data parse."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Read the file and parse the data.

        Arguments:
            path {str} -- path where the pdf file exists.
        """
        if not cls.can_ingest(path):
            raise Exception(f'Problem ingesting .pdf file.'
                f'Please check for correct format/corrupt file.')
            
        tmp = f'./{random.randint(0,100000000)}.txt'

        #pdftotext = r"C:\xpdf-tools-win-4.03\bin32\pdftotext.exe"
        #call = subprocess.call([pdftotext, '-layout', path, tmp])
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_Quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_Quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
