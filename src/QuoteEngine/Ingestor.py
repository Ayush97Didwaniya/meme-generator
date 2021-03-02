"""Ingestor class encapsulate the helper classes."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Calls the helper class & parse the file according to file type."""

    importers = [DocxIngestor, CSVIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Read the file and Parse the data."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
        return []
