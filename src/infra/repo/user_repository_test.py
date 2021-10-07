from faker import Faker

from .user_repository import UserRepository
from src.infra.config import DBConnectionHandler

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute(
        f"SELECT * FROM users WHERE id={new_user.id}"
    ).fetchone()
    engine.execute(f"DELETE FROM users WHERE id={new_user.id}")
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
