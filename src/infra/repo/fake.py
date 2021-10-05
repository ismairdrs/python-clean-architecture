# pylint: disable = E1101
from src.infra.config import DBConnectionHandler
from src.entities import User


class FakeRepo:
    """A simple repository"""

    @classmethod
    def insert_user(cls, name: str, password: str):
        """teste"""
        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(name="programador", password="idiota")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
