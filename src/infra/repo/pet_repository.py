from typing import List

from src.domain.models import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel
from src.data.interfaces import PetRepositoryInterface


class PetsRepository(PetRepositoryInterface):
    """Pets repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """insert data in PetsEntity entity"""
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            else:
                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )
            finally:
                db_connection.session.close()

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """select data in PetsEntity entitity by id and or user_id"""
        with DBConnectionHandler() as db_connection:
            try:
                query_data = None
                if pet_id and not user_id:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id)
                        .one()
                    )
                    query_data = [data]
                elif not pet_id and user_id:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data
                elif all([pet_id, user_id]):
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]
            except:
                db_connection.session.rollback()
                raise
            else:
                return query_data
            finally:
                db_connection.session.close()
