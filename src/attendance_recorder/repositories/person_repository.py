from typing import override

from core import BasePerson, IPersonRepository


class PersonRepository(IPersonRepository):
    @override
    def get(self, person_id: int) -> BasePerson | None:
        return super().get(person_id)

    @override
    def add(self, person: BasePerson) -> BasePerson:
        return super().add(person)

    @override
    def update(self, person: BasePerson) -> None:
        return super().update(person)

    @override
    def delete(self, person_id: int) -> bool:
        return super().delete(person_id)
