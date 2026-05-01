"""Classes for attendance objects.

Provides:
    AttendanceShema: base fields of attendance objects.
    BaseAttendance: base class for attendance.
    Attendance: attendance object.
    AttendanceUpdateDTO: DTO for attendance object.
"""

from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class AttendanceShema:
    """Represents attendance fields."""

    status: bool | None = None
    person_id: int | None = None
    event_id: int | None = None


@dataclass(frozen=True)
class AttendanceUpdateDTO(AttendanceShema):
    """Data transfer object for attendance."""


@dataclass
class BaseAttendance(ABC):
    """Represents base attendance info."""

    status: bool
    person_id: int
    event_id: int
    attendance_id: int | None = None


class Attendance(BaseAttendance):
    """Represents attendance info."""
