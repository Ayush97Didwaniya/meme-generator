"""Ingestor class encapsulate the helper classes."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .TXTImporter import TXTImporter
from .PDFImporter import PDFImporter


class Ingestor(IngestorInterface):
    """Calls the helper class & parse the file according to file type."""

    importers = [DocxImporter, CSVImporter, TXTImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Read the file and Parse the data."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                print(importer)
                return importer.parse(path)
        return []
