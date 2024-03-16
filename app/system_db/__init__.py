from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session,declarative_base
from config import Config

engine = create_engine(Config.DB_CONNECT)

db_session = scoped_session(sessionmaker(bind=engine,autocommit=False,autoflush=False,expire_on_commit=False))

Base = declarative_base()