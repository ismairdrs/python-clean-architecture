from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel
from .pet_repository import PetsRepository


faker = Faker()
pet_repository = PetsRepository()
db_connection = DBConnectionHandler()


def test_insert_pet():
    """should insert pet in Pets table and return it"""
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    new_pet = pet_repository.insert_pet(name, specie, age, user_id)
    engine = db_connection.get_engine()
    query_pet = engine.execute(f"SELECT * FROM pets WHERE id={new_pet.id}").fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id

    engine.execute(f"DELETE FROM pets WHERE id={new_pet.id}")
