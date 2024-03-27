from app.system_db import Base,engine
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,ForeignKey,PrimaryKeyConstraint

class Orders(Base):
    __tablename__ = "orders"
    order_id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(255),unique=True)
    body:Mapped[str] = mapped_column(String(25000))
    main_image:Mapped[str] = mapped_column(String(355))
    images:Mapped[str] = mapped_column(String(355))
    full_price:Mapped[float]
    price:Mapped[float]

class Users(Base):
    __tablename__ = "users"
    user_id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(255),default=None)
    email:Mapped[str] = mapped_column(unique=True)


class Comments(Base):
    __tablename__ = "comments"
    comment:Mapped[str] = mapped_column(String(2500))
    order_id:Mapped[int] = mapped_column(ForeignKey("orders.order_id",ondelete="CASCADE",onupdate="CASCADE"),primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.user_id",ondelete="CASCADE",onupdate="CASCADE"),primary_key=True)


class PayUsers(Base):
    __tablename__ = "pay_users"
    pay_id:Mapped[int] = mapped_column(primary_key=True)
    order_id:Mapped[int] = mapped_column(ForeignKey("orders.order_id",ondelete="CASCADE",onupdate='CASCADE'))
    steam_key:Mapped[str] = mapped_column(String(500))
    user_id:Mapped[int] = mapped_column(ForeignKey("users.user_id",ondelete="CASCADE",onupdate="CASCADE"))


Base.metadata.create_all(engine)