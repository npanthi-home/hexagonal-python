from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry
from entity.Employee import Employee

def map_employee():
    mapper_registry = registry()

    employee_table = Table(
        "employee",
         mapper_registry.metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('age', Integer),
        Column('department_id', Integer, ForeignKey('department.id')),
        Column('salary', Integer),
    )

    mapper_registry.map_imperatively(Employee, employee_table)