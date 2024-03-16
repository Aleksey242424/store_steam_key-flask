from app.system_db import Base,engine
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String

class Orders(Base):
    __tablename__ = "orders"
    order_id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(255),unique=True)
    body:Mapped[str] = mapped_column(String(25000))
    main_image:Mapped[str] = mapped_column(String(355))
    images:Mapped[str] = mapped_column(String(355))
    full_price:Mapped[float]
    price:Mapped[float]

Base.metadata.create_all(engine)