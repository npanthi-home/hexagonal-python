from typing import Optional
from injector import singleton, inject
from entity.Department import Department
from entity.Employee import Employee

from framework.mysql.SessionFactory import SessionFactory

@singleton
class EmployeeMysqlGateway:
    @inject
    def __init__(self, factory: SessionFactory) -> None:
        self.factory = factory

    def create(self, employee: Employee) -> Employee:
        session = self.factory.create_session()
        session.add(employee)
        session.commit()
        return Department

    def update(self, updatedEmployee: Employee) -> Employee:
        session = self.factory.create_session()
        existingEmployee = session.query(Employee).get(updatedEmployee.id)
        if existingEmployee:
            existingEmployee.name = updatedEmployee.name
            existingEmployee.age = updatedEmployee.age
            existingEmployee.department = updatedEmployee.department
            existingEmployee.salary = updatedEmployee.salary
            session.commit()
            return existingEmployee
        else:
            print("Employee with id {} not found".format(updatedEmployee.id))
            return None

    def delete(self, employee_id: str) -> bool:
        session = self.factory.create_session()
        employee = session.query(Employee).get(employee_id)
        if employee:
            session.delete(employee)
            session.commit()
            return True
        else:
            print("Employee with id {} not found".format(employee_id))
            return False

    def getById(self, employee_id: str) -> Employee:
        session = self.factory.create_session()
        employee = session.query(Employee).get(employee_id)
        return employee or None

    def getByDepartment(department_id: str) -> list[Employee]:
        pass
