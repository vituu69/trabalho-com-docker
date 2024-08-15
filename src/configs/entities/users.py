from sqlalchemy import Column, String, Integer
from src.configs import base

class Users[base]:

    __tablename__ = 'users'

    id = Column(Integer, pryimary_key=True)
    name = Column(String)

    def __repr__(self) -> str:
        return f'Users [name={self.name}]'