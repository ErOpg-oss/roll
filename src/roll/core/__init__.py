"""Core project classes: entities and interfaces."""

from roll.core.entities import (
    Attendance,
    AttendanceShema,
    AttendanceUpdateDTO,
    BaseAttendance,
    BaseEvent,
    BaseIdentifier,
    BasePerson,
    CardIdentifier,
    Event,
    EventShema,
    EventUpdateDTO,
    IdentifierShema,
    IdentifierUpdateDTO,
    Person,
    PersonShema,
    PersonUpdateDTO,
    QRIdentifier,
)
from roll.core.init_database import init_database
from roll.core.interfaces import (
    IAttendanceRepository,
    IEventRepository,
    IIdentifierRepository,
    IPersonRepository,
)

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
    "IAttendanceRepository",
    "IEventRepository",
    "IIdentifierRepository",
    "IPersonRepository",
    "IdentifierShema",
    "IdentifierUpdateDTO",
    "Person",
    "PersonShema",
    "PersonUpdateDTO",
    "QRIdentifier",
    "init_database",
]
