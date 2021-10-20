from src.infra.config import DBConnectionHandler, db_base
from src.infra.entities import Users


class FakerRepo:
    """a single repository"""

    @classmethod
    def insert_use(cls):
        """something"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Ismair", password="password")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
            finally:
                db_connection.session.close()
