import os
import configparser
from injector import singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from framework.mysql.mapper.map_department import map_department
from framework.mysql.mapper.map_employee import map_employee
from framework.mysql.mapper.Base import Base

@singleton
class SessionFactory:
    def __init__(self) -> None:
        pool = self.__create_pool()
        self.session_creator = sessionmaker(bind=pool)
        self.__init_mappers()

    def create_session(self):
        return self.session_creator()

    def __create_pool(self):
        config = self.__load_config()
        engine = self.__create_engine(config)
        return QueuePool(
            creator=lambda: engine.connect(),
            pool_size=config.getint('mysql', 'pool_size'),
            max_overflow=config.getint('mysql', 'max_overflow'),
            timeout=config.getint('mysql', 'pool_timeout'),
        )

    def __init_mappers(self):
        map_department()
        map_employee()

    def __load_config(self):
        config_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
        config = configparser.ConfigParser()
        config.read(config_file)
        return config
    
    def __create_url(self, config):
        user = config.get('mysql', 'user')
        password = config.get('mysql', 'password')
        host = config.get('mysql', 'host')
        database = config.get('mysql', 'database')
        return f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

    def __create_engine(self, config):
        db_url = self.__create_url(config)
        engine = create_engine(db_url)
        Base.metadata.reflect(bind=engine)
        return engine
