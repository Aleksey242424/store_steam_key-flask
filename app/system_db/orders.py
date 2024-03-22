from app.system_db import db_session
from app.system_db.models import Orders
from random import randint
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_

class CRUDOrders:
    @staticmethod
    def add(title:str,body:str,path_main_image:str,path_images:str,price:int):
        with db_session() as session:
            try:
                session.add(Orders(title=title,
                                body=body,
                                main_image=path_main_image,
                                images=path_images,
                                price=price,
                                full_price = randint(price,price+1000)
                                ))
                session.commit()
            except IntegrityError:
                session.rollback()

    @staticmethod
    def get(page):
        with db_session() as session:
            orders = session.query(Orders).offset(page*10-10).limit(10)
            return orders
        
    @staticmethod
    def get_order(order_id):
        with db_session() as session:
            order = session.query(Orders).filter_by(order_id = order_id).one_or_none()
            return order
        
    @staticmethod
    def get_order_for_redis():
        with db_session() as session:
            orders = session.query(Orders).order_by(Orders.order_id.asc())
            for order in orders:
                yield order

    @staticmethod
    def search_orders(search):
        with db_session() as session:
            orders = session.query(Orders.order_id).filter(
                or_(
                    Orders.title.ilike("%"+search+"%"),
                    Orders.body.ilike("%"+search+"%")
                    )
            ).all()
            return orders

