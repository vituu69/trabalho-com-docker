from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

class DBconnectio:

    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:123456@vic_banc/test'
        self.session = None

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()