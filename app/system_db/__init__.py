from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session,declarative_base

engine = create_engine("postgresql+psycopg2@postgres:123/store_stem_key")

db_session = scoped_session(sessionmaker(bind=engine,autocommit=False,autoflush=False,expire_on_commit=False))

Base = declarative_base()