from typing import Optional
from injector import singleton, inject
from entity.Department import Department

from framework.mysql.SessionFactory import SessionFactory

@singleton
class DepartmentMysqlGateway:
    @inject
    def __init__(self, factory: SessionFactory) -> None:
        self.factory = factory

    def create(self, department: Department) -> Department:
        session = self.factory.create_session()
        session.add(department)
        session.commit()
        return Department

    def update(self, updatedDepartment: Department) -> Optional[Department]:
        session = self.factory.create_session()
        existingDepartment = session.query(Department).get(updatedDepartment.id)
        if existingDepartment:
            existingDepartment.name = updatedDepartment.name
            existingDepartment.employee_count = updatedDepartment.employee_count
            session.commit()
            return existingDepartment
        else:
            print("Department with id {} not found".format(updatedDepartment.id))
            return None

    def delete(self, department_id: str) -> bool:
        session = self.factory.create_session()
        department = session.query(Department).get(department_id)
        if department:
            session.delete(department)
            session.commit()
            return True
        else:
            print("Department with id {} not found".format(department_id))
            return False

    def get(self, department_id: str) -> Optional[Department]:
        session = self.factory.create_session()
        department = session.query(Department).get(department_id)
        return department or None