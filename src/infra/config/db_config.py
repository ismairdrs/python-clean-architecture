from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """sqlalchemy"""

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """return connection engine"""
        return create_engine(self.__connection_string)

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
