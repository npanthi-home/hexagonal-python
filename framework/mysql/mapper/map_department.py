from sqlalchemy.orm import mapper
from entity.Department import Department
from framework.mysql.mapper.Base import Base

def map_department():
    mapper(
        Department,
        Base.metadata.tables['department'],
        properties={
            'id': Base.metadata.tables['department'].c.id,
            'name': Base.metadata.tables['department'].c.name,
            'employee_count': Base.metadata.tables['department'].c.employee_count,
        }
    )