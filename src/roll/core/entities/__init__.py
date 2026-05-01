"""Classes for entities.

Provides:
    AttendanceShema, BaseAttendance,
    Attendance, AttendanceUpdateDTO for attendance data.

    EventShema, BaseEvent,
    Event, EventUpdateDTO for event data.

    IdentifierShema, BaseIdentifier,
    Identifier, IdentifierUpdateDTO for identifier data.

    PersonShema, BasePerson,
    Person, PersonUpdateDTO for person data.
"""

from roll.core.entities.attendance import (
    Attendance,
    AttendanceShema,
    AttendanceUpdateDTO,
    BaseAttendance,
)
from roll.core.entities.event import BaseEvent, Event, EventShema, EventUpdateDTO
from roll.core.entities.identifier import (
    BaseIdentifier,
    CardIdentifier,
    IdentifierShema,
    IdentifierUpdateDTO,
    QRIdentifier,
)
from roll.core.entities.person import BasePerson, Person, PersonShema, PersonUpdateDTO

__all__ = [
    "Attendance",
    "AttendanceShema",
    "AttendanceUpdateDTO",
    "BaseAttendance",
    "BaseEvent",
    "BaseIdentifier",
    "BasePerson",
    "CardIdentifier",
    "Event",
    "EventShema",
    "EventUpdateDTO",
    "IdentifierShema",
    "IdentifierUpdateDTO",
    "Person",
    "PersonShema",
    "PersonUpdateDTO",
    "QRIdentifier",
]
