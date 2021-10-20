from faker import Faker
from src.infra.config import DBConnectionHandler
from src.domain.models import Pets
from src.entities.pets import AnimalTypes
from .pets_repository import PetsRepository

faker = Faker()
pet_repository = PetsRepository()
db_connection_handler = DBConnectionHandler()


def test_select_pet():
    """Should select a pet in Pets table and compare it"""

    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    specie_mock = AnimalTypes("fish")
    data = Pets(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    # SQL COmmands

    engine = db_connection_handler.get_engine()
    VALUES = f"('{pet_id}', '{name}', '{specie}', '{age}', '{user_id}')"
    engine.execute(
        f"INSERT INTO pets (id, name, specie, age, user_id) VALUES {VALUES};"
    )
    query_pets1 = pet_repository.select_pet(pet_id=pet_id)
    query_pets2 = pet_repository.select_pet(user_id=user_id)
    query_pets3 = pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

    assert data in query_pets1
    assert data in query_pets2
    assert data in query_pets3

    engine.execute(f"DELETE FROM pets WHERE id='{pet_id}';")
