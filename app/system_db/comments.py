from app.system_db import db_session
from app.system_db.models import Comments,Users
from sqlalchemy.exc import IntegrityError


class CRUDComments:
    @staticmethod
    def add(user_id,order_id,comment):
        with db_session() as session:
            try:
                session.add(Comments(user_id=user_id,order_id=order_id,comment=comment))
                session.commit()
            except IntegrityError:
                return 
            
    @staticmethod
    def update(user_id,order_id,comment):
        with db_session() as session:
            comment_obj = session.query(Comments).filter_by(user_id=user_id,order_id=order_id).scalar()
            comment_obj.comment = comment
            session.commit()

    @staticmethod
    def get_user_comment(user_id,order_id):
        with db_session() as session:
            return session.query(Comments).filter_by(user_id=user_id,order_id=order_id).scalar()

    @staticmethod
    def get(order_id):
        with db_session() as session:
            comments = session.query(Comments,Users).join(
                Users,Comments.user_id == Users.user_id
                                                    ).filter(Comments.order_id==order_id).all()
            return comments