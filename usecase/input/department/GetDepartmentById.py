from injector import inject, singleton
from entity.Department import Department
from usecase.output.DepartmentEntityGateway import DepartmentEntityGateway

@singleton
class GetDepartmentById:
    @inject
    def __init__(self, gateway: DepartmentEntityGateway):
        self.gateway = gateway

    def execute(self, department_id: str) -> Department:
        return self.gateway.get(department_id)