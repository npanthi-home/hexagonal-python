from typing import Protocol
from entity.Department import Department

class DepartmentEntityGateway(Protocol):
    def create(department: Department):
        ...

    def update(department: Department):
        ...

    def delete(department_id: str):
        ...

    def get(department_id: str):
        ...