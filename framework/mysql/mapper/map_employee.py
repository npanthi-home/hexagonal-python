from sqlalchemy.orm import mapper, relationship
from entity.Department import Department
from entity.Employee import Employee
from framework.mysql.mapper.Base import Base

def map_employee():
    mapper(
        Employee,
        Base.metadata.tables['employee'],
        properties={
            'id': Base.metadata.tables['employee'].c.id,
            'name': Base.metadata.tables['employee'].c.name,
            'age': Base.metadata.tables['employee'].c.age,
            'department': relationship(Department),
            'salary': Base.metadata.tables['employee'].c.salary,
        }
    )