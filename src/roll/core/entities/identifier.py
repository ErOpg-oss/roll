"""Classes for identifier objects.

Provides:
    IdentifierShema: base fields of identifier objects.
    BaseIdentifier: base class for identifier.
    Identifier: identifier object.
    IdentifierUpdateDTO: DTO for identifier object.
"""

from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class IdentifierShema:
    """Represents identifier fields."""

    person_id: int | None = None
    hash_value: str | None = None


@dataclass(frozen=True)
class IdentifierUpdateDTO(IdentifierShema):
    """Data transfer object for identifier."""


@dataclass
class BaseIdentifier(ABC):
    """Represents base identifier info."""

    identifier_id: int
    person_id: int
    hash_value: str


class QRIdentifier(BaseIdentifier):
    """Represents qr info."""


class CardIdentifier(BaseIdentifier):
    """Represents id-card info."""
