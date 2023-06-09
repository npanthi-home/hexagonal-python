from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry
from entity.Department import Department

def map_department():
    mapper_registry = registry()

    department_table = Table(
        "department",
        mapper_registry.metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('employee_count', Integer),
    )

    mapper_registry.map_imperatively(Department, department_table)