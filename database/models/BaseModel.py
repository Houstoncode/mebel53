from dotenv import dotenv_values
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class BaseModel(object):
    def __init__(self):

        config = dotenv_values(".env")
        self._engine = create_engine(f"mysql+mysqldb://{config.get('USERNAME_MYSQL')}:{config.get('PASSWORD_MYSQL')}@{config.get('HOSTNAME_MYSQL')}/{config.get('DATABASE_MYSQL')}")
        self._Session = sessionmaker(bind=self._engine)
        self._session = self._Session()
        self._session.execute(text("SET NAMES utf8"))
