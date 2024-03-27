from os import getenv,urandom,path
from dotenv import load_dotenv

class Config:
    load_dotenv()
    DEBUG = True
    SECRET_KEY = urandom(20)
    PATH_ORDERS = getenv("PATH_ORDERS")
    abs_path_static = path.abspath("app/static/")
    UPLOAD_ORDERS = getenv("UPLOAD_ORDERS")
    DB_DIALECT = getenv("DB_DIALECT")
    DB_API = getenv("DB_API")
    DB_USERNAME = getenv("DB_USERNAME")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_HOST = getenv("DB_HOST")
    DB_PORT = getenv("DB_PORT")
    DB_NAME = getenv("DB_NAME")
    DB_CONNECT = f"{DB_DIALECT}+{DB_API}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    MAIL_SERVER = getenv("MAIL_SERVER")
    MAIL_PORT = getenv("MAIL_PORT")
    MAIL_USE_TLS = getenv("MAIL_USE_TLS")
    MAIL_PASSWORD = getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = getenv("MAIL_DEFAULT_SENDER")
    MAIL_USERNAME = getenv("MAIL_USERNAME")
    
