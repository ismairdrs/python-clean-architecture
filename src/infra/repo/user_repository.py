from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from src.domain.models import Users


class UserRepository:
    """User repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """insert data in user entity"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            else:
                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            finally:
                db_connection.session.close()
