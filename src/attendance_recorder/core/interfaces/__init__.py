"""Interfaces for services and repositories.

Provides:
    IAttendanceRepository
    IEventRepository
    IIdentifierRepository
    IPersonRepository
"""

from core.interfaces.repositories import (
    IAttendanceRepository,
    IEventRepository,
    IIdentifierRepository,
    IPersonRepository,
)

__all__ = [
    "IAttendanceRepository",
    "IEventRepository",
    "IIdentifierRepository",
    "IPersonRepository",
]
