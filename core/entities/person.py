"""Classes for person objects.

Provides:
    PersonShema: base fields of person objects.
    BasePerson: base class for person.
    Person: person object.
    PersonUpdateDTO: DTO for person object.
"""

from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class PersonShema:
    """Represents person fields."""

    label: str | None = None
    description: str | None = None


@dataclass(frozen=True)
class PersonUpdateDTO(PersonShema):
    """Data transfer object for person."""


@dataclass
class BasePerson(ABC):
    """Represents base person info."""

    label: str
    description: str
    person_id: int | None = None


class Person(BasePerson):
    """Represents person info."""
