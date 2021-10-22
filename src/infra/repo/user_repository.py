from typing import List
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from src.domain.models import Users
from src.data.interfaces import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
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

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """select data in user entity by id and or name"""

        with DBConnectionHandler() as db_connection:
            try:
                query_data = None
                if user_id and not name:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]
                elif not user_id and name:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]
                elif all([user_id, name]):
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
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
