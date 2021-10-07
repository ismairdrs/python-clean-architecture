from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.entities import User


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> User:
        """insert data in user entity
        :param - name: person name ->
               - password: user password
        :return - tuple with new user inserted
        """
        InsertData = namedtuple("User", "id, name, password")
        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return InsertData(new_user.id, new_user.name, new_user.password)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
