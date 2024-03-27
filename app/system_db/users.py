from app.system_db.models import Users
from app.system_db import db_session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

class CRUDUsers:
    @staticmethod
    def add(email):
        with db_session() as session:
            try:
                session.add(Users(email=email))
                session.commit()
            except IntegrityError:
                session.rollback()

    @staticmethod
    def get_user_id(email):
        with db_session() as session:
            user_id = session.query(Users.user_id).filter_by(email=email).scalar()
            return user_id
        
    @staticmethod
    def update_username(user_id,username):
        with db_session() as session:
            session.query(Users).filter_by(user_id=user_id).update({"username":username})
            session.commit()

    @staticmethod
    def get_username(user_id):
        with db_session() as session:
            user = session.get(Users,user_id)
            return user.username