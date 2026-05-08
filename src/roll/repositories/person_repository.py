import logging
from typing import cast, override

from PySide6.QtSql import QSqlQuery

from roll.core import BasePerson, IPersonRepository, Person, PersonUpdateDTO
from roll.repositories.base_qsqlite_repository import BaseQtSQLiteRepository
from roll.repositories.exceptions import DTOValueError

logger = logging.getLogger(__name__)


class PersonRepository(IPersonRepository, BaseQtSQLiteRepository):
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

            return Person(p_id, p_label, p_desc)

        return None

    @override
    def get_all(self) -> tuple[BasePerson, ...]:
        query = QSqlQuery()

        sql = """
        SELECT person_id, label, description
        FROM persons;
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        if not query.exec():
            self._raise_on_exec(query)

        persons: list[BasePerson] = []

        if query.next():
            p_id = cast("int", query.value(0))
            p_label = cast("str", query.value(1))
            p_desc = cast("str", query.value(2))

            persons += [Person(p_id, p_label, p_desc)]

        return tuple(persons)

    @override
    def add(self, person: PersonUpdateDTO) -> None:
        if not person.label:
            raise DTOValueError

        query = QSqlQuery()

        sql = """
        INSERT INTO persons (label, description)
        VALUES (:label, NULLIF(:description, ''))
        """

        if not query.prepare(sql):
            self._raise_on_prepare(query)

        query.bindValue("label", person.label)
        query.bindValue("description", person.description)

        if not query.exec():
            self._raise_on_exec(query)

    @override
    def update(self, person_id: int, person: PersonUpdateDTO) -> None:
        if person.label == "":
            raise DTOValueError

        query = QSqlQuery()

        sql = """
        UPDATE persons
        SET label = COALESCE(:label, label),
            description = COALESCE(NULLIF(:description, ''), description)
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
