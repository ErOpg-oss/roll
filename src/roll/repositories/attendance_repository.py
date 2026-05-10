import logging
from typing import TYPE_CHECKING, cast, override

from PySide6.QtSql import QSqlQuery

from roll.core import Attendance
from roll.core.interfaces import IAttendanceRepository
from roll.repositories.base_qsqlite_repository import BaseQtSQLiteRepository

if TYPE_CHECKING:
    from roll.core.entities import AttendanceUpdateDTO, BaseAttendance

logger = logging.getLogger(__name__)


class AttendanceRepository(IAttendanceRepository, BaseQtSQLiteRepository):
    def __init__(self) -> None:
        """Log message on repository init."""
        logger.info("Initialized attendance repository")

    @override
    def get(self, attendance_id: int) -> BaseAttendance | None:
        query = QSqlQuery()

        sql = """
        SELECT attendance_id, person_id, event_id, status
        FROM attendance
        WHERE attendance_id = (?);
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.addBindValue(attendance_id)

        if not query.exec():
            self._raise_on_exec(query)

        if query.next():
            return self._build_attendance(query)

        return None

    @override
    def add(self, attendance: AttendanceUpdateDTO) -> None:
        query = QSqlQuery()

        sql = """
        INSERT INTO attendance (person_id, event_id, status)
        VALUES (:person_id, :event_id, :status);
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.bindValue("person_id", attendance.person_id)
        query.bindValue("event_id", attendance.event_id)
        query.bindValue("status", attendance.status)

        if not query.exec():
            self._raise_on_exec(query)

    @override
    def update(self, attendance_id: int, attendance: AttendanceUpdateDTO) -> None:
        query = QSqlQuery()

        sql = """
        UPDATE attendance
        SET person_id = COALESCE(:person_id, person_id),
            event_id = COALESCE(:event_id, event_id),
            status = COALESCE(:status, status),
        WHERE attendance_id = :id;
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.bindValue("person_id", attendance.person_id)
        query.bindValue("event_id", attendance.event_id)
        query.bindValue("status", attendance.status)

        if not query.exec():
            self._raise_on_exec(query)

        if query.numRowsAffected() == 0:
            logger.warning("Record with ID %d is not found", attendance_id)

    @override
    def delete(self, attendance_id: int) -> bool:
        query = QSqlQuery()

        sql = """
        DELETE FROM attendance
        WHERE attendance_id = (?)
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.addBindValue(attendance_id)

        if not query.exec():
            self._raise_on_exec(query)

        if query.numRowsAffected() == 0:
            logger.warning("Record with ID %d is not found", attendance_id)
            return False

        return True

    @staticmethod
    def _build_attendance(query: QSqlQuery) -> BaseAttendance:
        a_id = cast("int", query.value(0))
        a_person_id = cast("int", query.value(1))
        a_event_id = cast("int", query.value(2))
        a_status = bool(cast("int", query.value(3)))

        return Attendance(
            a_id,
            a_person_id,
            a_event_id,
            a_status,
        )
