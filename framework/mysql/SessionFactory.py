import os
import configparser
from injector import singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from framework.mysql.mapper.map_department import map_department
from framework.mysql.mapper.map_employee import map_employee


@singleton
class SessionFactory:
    def __init__(self) -> None:
        pool = self.__create_pool()
        self.session_creator = sessionmaker(bind=pool)
        self.__init_mappers()

    def create_session(self):
        return self.session_creator()

    def __create_pool(self):
        config_file = os.path.join(os.path.dirname(__file__), 'framework', 'config', 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        user = self.config.get('mysql', 'user')
        password = self.config.get('mysql', 'password')
        host = self.config.get('mysql', 'host')
        database = self.config.get('mysql', 'database')
        db_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        return QueuePool(
            creator=lambda: create_engine(db_url).connect(),
            pool_size=self.config.getint('mysql', 'pool_size'),
            max_overflow=self.config.getint('mysql', 'max_overflow'),
            pool_timeout=self.config.getint('mysql', 'pool_timeout'),
        )

    def __init_mappers(self):
        map_department()
        map_employee()
