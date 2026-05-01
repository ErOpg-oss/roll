import logging
from typing import cast, override

from PySide6.QtSql import QSqlQuery

from roll.core import BasePerson, IPersonRepository, Person, PersonUpdateDTO
from roll.repositories.exceptions import QueryFailedExecError, QueryFailedPrepareError

logger = logging.getLogger(__name__)


class PersonRepository(IPersonRepository):
    def __init__(self) -> None:
        """Log message on repository init."""
        logger.info("Initialized person repository")

    @override
    def get(self, person_id: int) -> BasePerson | None:
        query = QSqlQuery()

        sql = """
        SELECT person_id, label, description
        FROM persons
        WHERE person_id = (?);
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.addBindValue(person_id)

        if not query.exec():
            self._raise_on_exec(query)

        if query.next():
            p_id = cast("int", query.value(0))
            p_label = cast("str", query.value(1))
            p_desc = cast("str", query.value(2))

            return Person(p_label, p_desc, p_id)

        return None

    @override
    def add(self, person: BasePerson) -> BasePerson:
        query = QSqlQuery()

        sql = """
        INSERT INTO persons (label, description)
        VALUES (:label, :description)
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.bindValue("label", person.label)
        query.bindValue("description", person.description)

        if not query.exec():
            self._raise_on_exec(query)

        return Person(
            person.label, person.description, cast("int", query.lastInsertId())
        )

    @override
    def update(self, person_id: int, person: PersonUpdateDTO) -> None:
        query = QSqlQuery()

        sql = """
        UPDATE persons
        SET label = COALESCE(:label, label),
            description = COALESCE(:description, description)
        WHERE person_id = :id
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.bindValue("label", person.label)
        query.bindValue("description", person.description)
        query.bindValue("id", person_id)

        if not query.exec():
            self._raise_on_exec(query)

        if query.numRowsAffected() == 0:
            logger.warning("Record with ID %d is not found", person_id)

    @override
    def delete(self, person_id: int) -> bool:
        query = QSqlQuery()

        sql = """
        DELETE FROM persons
        WHERE person_id = (?)
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.addBindValue(person_id)

        if not query.exec():
            self._raise_on_exec(query)

        if query.numRowsAffected() == 0:
            logger.warning("Record with ID %d is not found", person_id)
            return False

        return True

    @staticmethod
    def _raise_on_prepare(query: QSqlQuery) -> None:
        error = query.lastError().text()
        logger.error("SQL Error: %s", error)
        raise QueryFailedPrepareError(error)

    @staticmethod
    def _raise_on_exec(query: QSqlQuery) -> None:
        error = query.lastError().text()
        logger.error("SQL Error: %s", error)
        raise QueryFailedExecError(error)
