from .configs.init import DBconnectio
from .entities.users import Users as User_model

class User_repo:

    def insert_name(self, name):
        with DBconnectio() as dbconn:
            new_user = User_model(name=name)
            dbconn.session.add(new_user)
            dbconn.session.commit()
