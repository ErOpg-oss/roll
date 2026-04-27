"""Interfaces for repositories.

Provides:
    IAttendanceRepository,
    IEventRepository,
    IIdentifierRepository
    IPersonRepository,
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.entities import BaseAttendance, BaseEvent, BaseIdentifier, BasePerson


class IAttendanceRepository(ABC):
    """Interface for attendance repository."""

    @abstractmethod
    def get(self, attendance_id: int) -> BaseAttendance | None:
        """Finds and returns attendance by it's id.

        Returns None if attendance is not found.
        """

    @abstractmethod
    def add(self, attendance: BaseAttendance) -> BaseAttendance:
        """Saves new attendance in repository."""

    @abstractmethod
    def update(self, attendance: BaseAttendance) -> None:
        """Updates existing attendance info."""

    @abstractmethod
    def delete(self, attendance_id: int) -> bool:
        """Deletes attendance from repository.

        Returns bool if operation is successfull.
        """


class IEventRepository(ABC):
    """Interface for event repository."""

    @abstractmethod
    def get(self, event_id: int) -> BaseEvent | None:
        """Finds and returns event by it's id.

        Returns None if event is not found.
        """

    @abstractmethod
    def add(self, event: BaseEvent) -> BaseEvent:
        """Saves new event in repository."""

    @abstractmethod
    def update(self, event: BaseEvent) -> None:
        """Updates existing event info."""

    @abstractmethod
    def delete(self, event_id: int) -> bool:
        """Deletes event from repository.

        Returns bool if operation is successfull.
        """


class IPersonRepository(ABC):
    """Interface for person repository."""

    @abstractmethod
    def get(self, person_id: int) -> BasePerson | None:
        """Finds and returns person by it's id.

        Returns None if person is not found.
        """

    @abstractmethod
    def add(self, person: BasePerson) -> BasePerson:
        """Saves new person in repository."""

    @abstractmethod
    def update(self, person: BasePerson) -> None:
        """Updates existing person info."""

    @abstractmethod
    def delete(self, person_id: int) -> bool:
        """Deletes person from repository.

        Returns bool if operation is successfull.
        """


class IIdentifierRepository(ABC):
    """Interface for identifier repository."""

    @abstractmethod
    def get(self, identifier_id: int) -> BaseIdentifier | None:
        """Finds and returns identifier by it's id.

        Returns None if identifier is not found.
        """

    @abstractmethod
    def add(self, identifier: BaseIdentifier) -> BaseIdentifier:
        """Saves new identifier in repository."""

    @abstractmethod
    def update(self, identifier: BaseIdentifier) -> None:
        """Updates existing identifier info."""

    @abstractmethod
    def delete(self, identifier_id: int) -> bool:
        """Deletes identifier from repository.

        Returns bool if operation is successfull.
        """
