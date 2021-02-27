"""IngestorInterface Class define model for helper classes."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """A Simple Ingestor Class."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """To check if parser available for particular file type."""
        ext = path.split('.')[-1]
        print("ext", ext)
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To parse data."""
        pass