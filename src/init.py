from configs.init import DBconnectio
from src.configs.entities import users as user_model

class User_repo:

    def insert_name(self, name):
        with DBconnectio() as dbconn:
            new_user = user_model(name=name)
            dbconn.session.add(new_user)
            dbconn.session.commit()
