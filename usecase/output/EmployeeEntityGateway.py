from typing import Protocol
from entity.Employee import Employee

class EmployeeEntityGateway(Protocol):
    def create(employee: Employee) -> Employee:
        ...

    def update(employee: Employee) -> Employee:
        ...

    def delete(employee_id: str) -> bool:
        ...

    def getById(employee_id: str) -> Employee:
        ...

    def getByDepartment(department_id: str) -> list[Employee]:
        ...
