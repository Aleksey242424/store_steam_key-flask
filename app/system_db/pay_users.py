from app.system_db import db_session
from app.system_db.models import PayUsers

class CRUDPayUsers:
    @staticmethod
    def add(order_id,user_id,steam_key):
        with db_session() as session:
            session.add(PayUsers(order_id=order_id,user_id=user_id,steam_key=steam_key))
            session.commit()

    @staticmethod
    def get(user_id):
        with db_session() as session:
            orders_id = session.query(PayUsers).filter_by(user_id=user_id).all()
            return orders_id
        